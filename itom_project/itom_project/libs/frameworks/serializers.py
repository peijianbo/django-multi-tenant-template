from rest_framework import serializers


class ModifierModelSerializer(serializers.ModelSerializer):
    """Auto fill create_by/update_by field when save an instance"""
    def create(self, validated_data):
        validated_data['create_by'] = self.context.get('request').user_.username
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('create_by', None)
        validated_data['update_by'] = self.context.get('request').user_.username
        return super().update(instance, validated_data)

    def get_field_names(self, *args):
        """调整模型序列化时的字段顺序"""
        fields = super().get_field_names(*args)
        for field in ('create_by', 'update_by', 'create_time', 'update_time'):
            if field in fields:
                fields.remove(field)
                fields.append(field)
        return fields


class DisplayModelSerializer(serializers.ModelSerializer):
    """
    Add an extra field(named field_name+'_display') for describing ChoiceField.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in list(self.fields.items()):
            if isinstance(field, serializers.ChoiceField):
                self.fields[field_name+'_display'] = serializers.CharField(
                    source=f'get_{field_name}_display',
                    read_only=True,
                    label=field.label,
                    help_text=field.help_text
                )
