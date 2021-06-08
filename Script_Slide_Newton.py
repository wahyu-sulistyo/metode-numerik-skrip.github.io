import sys
import traceback


class InterpolateNewton:
    X = [0.0, 0.1, 0.2, 0.3, 0.4]
    Y = [0.0, 0.099833417, 0.198669331, 0.295520207, 0.389418342]

    def __init__(self):
        self.n = len(self.X)

    def compute(self):
        """ Computation of interpolation with Newton method """
        try:
            print("      x      y")
            for a in range(int(self.X[-1]) * 2 + 1):
                t = 0.5 * a
                print("{:7.2f}{:7.2f}".format(t, self.__interpolate(t)))
        except Exception as e:
            raise

    def __interpolate(self, t):
        """ Interpoalation with Newton method
        :param float t
        """
        try:
            c = [0 for _ in range(self.n)]
            w = [0 for _ in range(self.n)]
            for i in range(0, self.n):
                w[i] = self.Y[i]
                for j in reversed(range(i)):
                    w[j] = (w[j + 1] - w[j]) / (self.X[i] - self.X[j])
                c[i] = w[0]
            s = c[self.n - 1]
            for i in reversed(range(self.n - 1)):
                s = s * (t - self.X[i]) + c[i]
            return s
        except Exception as e:
            raise


if __name__ == '__main__':
    try:
        obj = InterpolateNewton()
        obj.compute()
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)