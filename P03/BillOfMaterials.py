from BillOfMaterialsProvider import BillOfMaterialsProvider

class BillOfMaterials:
    def __init__(self) -> None:
        self.api = BillOfMaterialsProvider()
    
    def print_bill(self) -> None:
        df = self.api.get_data()
        s = ''

        for index in df.index:
            material = df['material'][index]
            cost = df['cost'][index]
            s += '{position} | {cost} \n'.format(
                position=BillOfMaterials.format_position(material), 
                cost=BillOfMaterials.format_cost(cost)
            )

        s += '----------------+----------\n'
        s += '{position} | {total}'.format(
            position=BillOfMaterials.format_position('SUM'), 
            total=BillOfMaterials.format_cost(self.api.get_total())
        )
        
        print(s)
            
    def format_cost(cost) -> str:
        return format(cost, '.2f')

    def format_position(p) -> str:
        return '{:<15}'.format(p)

if __name__ == '__main__':
    bom = BillOfMaterials()
    bom.print_bill()
    