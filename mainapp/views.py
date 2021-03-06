from distutils.util import strtobool

from rest_framework import views
from rest_framework.response import Response


class MortgageViewSet(views.APIView):

    # Аннуитетный метод
    @staticmethod
    def get_annuity_mortgage(sum, period, rate):

        month_rate = rate / 12
        top_part = (sum * month_rate)
        bottom_part = (1 - (1 / (month_rate + 1) ** period))
        ann = (top_part / bottom_part)
        return Response(ann)

    # Дифференцированный метод
    @staticmethod
    def get_differentiated_mortgage(sum, period, rate):
        remain_summa = sum
        month_rate = rate / 12
        main_debt = +(sum / period)
        response = []

        for i in range(period):
            remain_summa_old = remain_summa
            percent = remain_summa * month_rate
            remain_summa -= main_debt
            dif = percent + main_debt
            response.append({
                'old_debt': remain_summa_old,
                'percent': percent,
                'main_debt': main_debt,
                'payment': dif,
            })
        return Response(response)

    # get метод
    def get(self, request, *args, **kwargs):
        # Получение параметров body
        # sum = int(self.request.data['sum'])
        # period = int(self.request.data['period'])
        # rate = float(self.request.data['rate'])
        # is_diff = strtobool(self.request.data['is_diff'])
        sum = int(self.request.GET['sum'])
        period = int(self.request.GET['period'])
        rate = float(self.request.GET['rate'])
        is_diff = strtobool(self.request.GET['is_diff'])
        # Вызов метода в зависимости от типа рассчета
        if is_diff:
            return self.get_differentiated_mortgage(sum, period, rate)
        return self.get_annuity_mortgage(sum, period, rate)
