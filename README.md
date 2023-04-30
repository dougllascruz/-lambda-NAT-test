## lambda-NAT-test
Com a crescente utilização de microsserviços sem servidor no AWS Lambda, o que é ótimo para executar serviços da Web sem estado na nuvem que não precisam que seus servidores da Web estejam em execução contínua. O AWS Lambda oferece escalabilidade fácil e alta disponibilidade para o código do seu aplicativo sem qualquer esforço ou responsabilidade de você gerenciar e provisionar instâncias do EC2, algumas organizações ainda usam [IP Whitelisting](https://en.wikipedia.org/wiki/Whitelisting) para permitir o acesso aos seus serviços.

O AWS Lambda oferece suporte à atribuição de sua função Lambda a uma VPC, com sub-redes VPC e grupos de segurança correspondentes, [mais informações](https://docs.aws.amazon.com/lambda/latest/dg/vpc.html). Se o seu VPC estiver configurado com sub-redes privadas, sem acesso externo, eles normalmente serão configurados com um NAT para quaisquer rotas externas.

Normalmente eu configuro uma abordagem de 3 camadas.

1. Rede externa -- (para balanceadores de carga, ALB, NLB e ELB) Isso usará o gateway VPC para roteamento
2. Rede de aplicativos -- para serviços de aplicativos, ECS, etc. Não terá acesso externo direto e usará um NAT para qualquer chamada de aplicativo externo.
3. Rede de dados -- para todos os bancos de dados, RDS, etc. Isso normalmente não tem NAT e não deve precisar fazer chamadas externas.
</br>

### Lambda Functions
Criei as seguintes funções do Lambda para testar a configuração de VPC e NAT, bem como testar a conectividade com quaisquer serviços externos que possam usar a lista de permissões de IP.


[lambda-NAT-test.py](lambda-NAT-test.py) -- Chamadas de Função [ifconfig.me](https://ifconfig.me) e retorna o IP NAT usado na chamada.

[lambda-port-test.py](lambda-port-test.py) -- Em Breve

[lambda-NAT-Port-test.py](lambda-NAT-Port-test.py) -- Em Breve
