#wenn Display = x Zoll, dann y Vesa Maße 200x200 oder 400x400
#wenn chief-Halterung in Center position (Diamond kerbe in halter), dann ist Center zu oberem Loch IMMER 203.2mm
#Beispiel:
#Bei 75" Displayhoehe CenterVesa = Unterkante Display + 960mm - 265.6mm - 200mm, wäre dann Center der VESA Halterung.
#oberesLoch = CenterVesa + 203.2mm
#unteresLoch = oberesLoch - 406.4mm

def main():
    Displayzoll = input('Displaygroesse eingeben: ')

    if Displayzoll == '75':
        Displayhoehe = float(960)
        print("Die Displayhoehe beträgt", Displayhoehe, end=' mm\n')
        print("VesaStandard: 400x400(mm)")
        print("Bitte darauf achten, dass Chief-Halterung in der Center-Position ist!")

    elif Displayzoll == '32':
            Displayhoehe = float(419.61)
            print("VesaStandard: 200x200(mm)")
            print("Bitte darauf achten, dass Chief-Halterung in der Center-Position ist!")

    elif Displayzoll == '65':
            Displayhoehe = float(831)
            print("Die Displayhoehe betraegt", Displayhoehe, end=' mm\n')
            print("VesaStandard: 400x400(mm)")
            print("Bitte darauf achten, dass Chief-Halterung in der Center-Position ist!")

    elif Displayzoll == '55':
        Displayhoehe = float(707.9)
        print("Die Displayhoehe betraegt", Displayhoehe, end=' mm\n')
        print("VesaStandard: 200x200(mm)")
        print("Bitte darauf achten, dass Chief-Halterung in der Center-Position ist!")

    else:
        print("Keine gültigen Maße eingegeben!")

    unter_Display = float(input("Unterkante Display in cm: "))
    centerVesa = float(unter_Display * 10 + Displayhoehe - 256.6 - 200)

    oberesLoch = centerVesa + 203.2
    unteresLoch = oberesLoch - 406.4

    print("Das Center des Vesa-Standards betraegt: %3.2f " %centerVesa)
    print("Die oberen Löcher befinden sich auf einer Hoehe von: %3.0f " %oberesLoch, end='mm\n')
    print("Die unteren Löcher befinden sich auf einer Hoehe von: %3.0f" %unteresLoch, end=' mm')

if __name__ == "__main__":
    main()