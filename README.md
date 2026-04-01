# pyvisa_agilent_33500B_waveform_gen
A pysvisa driver for the Agilent 33500B Waveform generator


A implementação que faremos abaixo terá como base o vídeo abaixo:
https://www.youtube.com/watch?v=zi6QYYljCCs&pp=ygUbd2F2ZWZvcm0gZ2VuIGFnaWxlbnQgcHl2aXNh

1* Ponto importante, precisamos garantir que nosso dispositivo está conectado a rede, para isso iremos rodar um comando ping, neste caso farei um ping de 5 tentativas:


```bash
ping -c n_de_pings ip_do dispositivo

```
Nosso aparelho está com o ip reservado de 10.128.15.200, portanto:

```bash
ping -c 5 10.128.16.126
```

Com isso obtivemos esta amostra:


```bash
matheus@matheus-Vivobook-Go-E1504FA-E1504FA:~/pyvisa_agilent_33500B_waveform_gen$ ping -c 5 10.128.16.126
PING 10.128.16.126 (10.128.16.126) 56(84) bytes of data.
64 bytes from 10.128.16.126: icmp_seq=1 ttl=128 time=5.10 ms
64 bytes from 10.128.16.126: icmp_seq=2 ttl=128 time=2.26 ms
64 bytes from 10.128.16.126: icmp_seq=3 ttl=128 time=1.99 ms
64 bytes from 10.128.16.126: icmp_seq=4 ttl=128 time=2.07 ms
64 bytes from 10.128.16.126: icmp_seq=5 ttl=128 time=4.32 ms

--- 10.128.16.126 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4005ms
rtt min/avg/max/mdev = 1.986/3.146/5.095/1.301 ms
```

Portanto a conexão lan está funcionando!

Afim de confirmar se o dispositivo apontado é o nosso iremos rodar um teste por telnet:

```bash
matheus@matheus-Vivobook-Go-E1504FA-E1504FA:~/pyvisa_agilent_33500B_waveform_gen$ telnet 10.128.16.126 5024
Trying 10.128.16.126...
Connected to 10.128.16.126.
Escape character is '^]'.
Welcome to Agilent's 33500-Series Waveform Generator
33500> 
```

De fato o dispositivo encontrado é o nosso gerador de funções na bancada.

E agora já é possível iniciar nosso clock de bancada de 2Mhz com tensão de 3V de amplitutde, 50% de duty 
---
Para usar o script basta chamar (com o venv ativo):
```bash
python agilent_33500b_wg.py
```

(pyvisa_venv) matheus@matheus-Vivobook-Go-E1504FA-E1504FA:~/pyvisa_agilent_33500B_waveform_gen$ python agilent_33500b_wg.py
Instrument: Agilent Technologies,33522B,MY52802702,2.09-1.19-2.00-52-00
Clock configurado com sucesso.
Frequência : 2000000 Hz
Nível alto : 3.3 V
Nível baixo: 0.0 V
Duty cycle : 50.0 %
SCPI error 1: +0,"No error"


Imagens do teste:

<div align="center">

| **Fluxo de simulação** |
| :---: |
| **Defini a escala manualmente no múltimetro como corrente DC apenas para ficar diferente do que queremos** |
![Defini a escala manualmente no múltimetro como corrente DC apenas para ficar diferente do que queremos](https://github.com/MattGrossi12/pyvisa_agilent_33500B_waveform_gen/blob/main/images/img1.png)
| **Chamamos o script python** |
![Chamos o script python](https://github.com/MattGrossi12/pyvisa_agilent_33500B_waveform_gen/blob/main/images/img2.png)
| **O gerador de funções então aplica os parâmetros que definimos no header:** |
![O gerador de funções então aplica os parâmetros que definimos no header:](https://github.com/MattGrossi12/pyvisa_agilent_33500B_waveform_gen/blob/main/images/img3.png)

<div align="justify">

Link do vídeo:
[Teste](https://github.com/MattGrossi12/pyvisa_agilent_33500B_waveform_gen/blob/main/teste/teste.mp4)
