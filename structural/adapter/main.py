# JSON - int
# XML - str

class Old:
    def get(self) -> str:
        return "1234"


class New:
    def get(self) -> int:
        return 1234


class Adapter(New):
    def get(self):
        return str(super(Adapter, self).get())


def main(obj):
    print("Result: " + obj.get())


if __name__ == '__main__':
    obj = Old()
    main(obj)
    obj = Adapter()
    main(obj)
