from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ActionType(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Action(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    action_type = models.ForeignKey(ActionType, on_delete=models.CASCADE)
    data = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.patient}: {self.time}: {self.action_type}: {self.data}"


class Rule(models.Model):
    ALERT_TYPES = [
        ('danger', "Critical"),
        ('success', 'Success'),
        ('warning', 'Warning'),
        ('info', 'Info'),
    ]
    priority = models.IntegerField(default=0)
    text = models.CharField(max_length=100)
    alert_message = models.CharField(max_length=100)
    alert_type = models.CharField(max_length=10, choices=ALERT_TYPES)
    function_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.priority}: {self.text}"


class Alert(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=100)
    alert_type = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.patient}: {self.time}: {self.message}"


class Setting(models.Model):
    monitor = models.BooleanField(default=False)
    monitor_time = models.IntegerField(default=60)

    def __str__(self):
        return f"Monitoring: {'ON' if self.monitor else 'OFF'} ({self.monitor_time} seconds)"