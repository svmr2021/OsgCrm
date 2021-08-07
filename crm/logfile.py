from .models import *


def logfile(creator,type,validated_data):
    if type == 'Create_user':
        role = validated_data.get('role')
        if role == 'Employee':
            user = 'Сотрудника'
        elif role == 'Accountant':
            user = 'Бухгалтера'
        elif role == 'Leader':
            user = 'Руководителя'
        else:
            user = None

        if user is not None:
            text = f'{creator.full_name} добавил {user}'
            action = Action.objects.create(executor=creator,type = type, text=text)
            action.save()
    elif type == 'Edit_user':
        name = validated_data.get('first_name') +  ' ' + validated_data.get('last_name') + ' ' + validated_data.get('middle_name')
        text = f'{creator.full_name} изменил личные данные {name}'
        action = Action.objects.create(executor=creator,type=type,text=text)
        action.save()
    elif type == 'Add_salary':
        client = validated_data.get('user')
        amount = validated_data.get('amount')
        salary_type = validated_data.get('salary_type')
        text = f'{creator.full_name} добавил зарплату {client.full_name} в сумму {amount} {salary_type} '
        action = Action.objects.create(executor=creator,type=type,text=text)
        action.save()
    elif type == 'Edit_salary':
        amount = validated_data.get('amount')
        salary_type = validated_data.get('salary_type')
        client = validated_data.get('user')
        text = f'{creator.full_name} изменил зарплату {client.full_name} в сумму {amount} {salary_type}'
        action = Action.objects.create(executor=creator,type=type,text=text)
        action.save()
    elif type == 'Send_salary':
        client = validated_data.get('user')
        amount = validated_data.get('amount')
        payment_type = validated_data.get('payment_type')
        salary_type = validated_data.get('type')
        if salary_type == 'Salary':
            salary = 'зарплату'
        elif salary_type == 'Prepayment':
            salary = 'премию'
        elif salary_type == 'Penalty':
            salary = 'штраф'
        else:
            salary = None
        if salary is not None:
            text = f'{creator.full_name} отправил {salary} {client.full_name} в сумму {amount} {payment_type}'
            action = Action.objects.create(executor=creator, type=type, text=text)
            action.save()
    elif type == 'Accept_salary':
        instance = validated_data.get('instance')
        if instance.type == 'Salary':
            text = f'{creator.full_name} принял зарплату в сумму {instance.amount} {instance.payment_type}'
        elif instance.type == 'Prepayment':
            text = f'{creator.full_name} принял премию в сумму {instance.amount} {instance.payment_type}'
        elif instance.type == 'Penalty':
            text = f'{creator.full_name} принял штраф в сумму {instance.amount} {instance.payment_type}'
        else:
            text = None
        if text is not  None:
             action = Action.objects.create(executor=creator,type=type,text=text)
             action.save()
    elif type == 'Decline_salary':
        instance = validated_data.get('instance')
        if instance.type == 'Salary':
            text = f'{creator.full_name} отклонил зарплату в сумму {instance.amount} {instance.payment_type}'
        elif instance.type == 'Prepayment':
            text = f'{creator.full_name} отклонил премию в сумму {instance.amount} {instance.payment_type}'
        elif instance.type == 'Penalty':
            text = f'{creator.full_name} отклонил штраф в сумму {instance.amount} {instance.payment_type}'
        else:
            text = None
        if text is not None:
            action = Action.objects.create(executor=creator, type=type, text=text)
            action.save()