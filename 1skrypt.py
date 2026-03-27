# PLIK KONFIGURACYJNY DEVOPS / INFRASTRUKTURA JAKO KOD (IAC)

Resource: SecurityGroup-WebApp
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: Zabezpieczenia dla serwera aplikacji webowej

    # 1. ZASADY RUCHU PRZYCHODZĄCEGO (INGRESS RULES)
    SecurityGroupIngress:

      # NIEBEZPIECZNA REGUŁA (STAN PIERWOTNY)
      # Stan, który musimy usunąć/zamknąć, aby zwiększyć bezpieczeństwo
      - IpProtocol: tcp
        FromPort: 22
        ToPort: 22
        CidrIp: 0.0.0.0/0 
        Description: "BLAD: Otwarte SSH dla wszystkich"

      # BEZPIECZNA REGUŁA (STAN DOCELOWY) - JAKI MA BYĆ
      - IpProtocol: tcp
        FromPort: 443
        ToPort: 443
        CidrIp: 0.0.0.0/0
        Description: "Dozwolony HTTPS (443) dla świata"

      # REGUŁA DOSTĘPU ADMINA (KRYTYCZNA)
      - IpProtocol: tcp
        FromPort: 22
        ToPort: 22
        # TUTAJ WDROŻYMY ZABEZPIECZENIE: Ograniczenie do jednego IP
        CidrIp: 203.0.113.55/32  
        Description: "Dozwolony SSH (22) tylko z IP Biura"