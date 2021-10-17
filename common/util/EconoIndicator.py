class EconoIndicator:
    @staticmethod
    def get_growth_rate(last, this):
        """
        :param last:
        :param this:
        :return: The unit of return value is percentage
        """
        if last == 0:
            return (this-1/abs(1)) * 100
        else:
            return ((this - last)/abs(last)) * 100