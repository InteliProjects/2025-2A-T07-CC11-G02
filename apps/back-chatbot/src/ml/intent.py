import random
from typing import ClassVar, Optional

from ..core.config import CONFIG


class Intent:
    use_rag: ClassVar[bool] = False
    rag_context: ClassVar[Optional[str]] = None

    def __init__(self, response: str):
        self.response = response

    def get_name(self):
        return CONFIG["user"]["name"]

    def should_use_rag(self) -> bool:
        return bool(self.use_rag)

    def get_rag_context(self) -> Optional[str]:
        return self.rag_context

    def prepare_rag_question(self, user_text: str) -> str:
        context = self.get_rag_context()
        clean_text = user_text.strip()
        if context:
            context = context.strip()
            if context:
                return f"{context}\n\nUsuário: {clean_text}"
        return clean_text

    def smart_fallback(self, user_text: str, *, reason: Optional[str] = None) -> str:
        name = self.get_name()
        return (
            f"Não encontrei informações suficientes agora, {name}. "
            "Posso acionar alguém do nosso time de atendimento ou você pode me contar um "
            "pouco mais para eu tentar novamente."
        )

    def get_products(self):
        return [
            "BLUSA MOLONA",
            "CALÇA COOL",
            "CAMISA DE PRESENÇA",
            "CAMISETA WOW",
            "MACACÃO TÔ PRONTA",
            "SAIA ACINTURANTE",
            "SAIA ALONGADORA",
            "VESTIDO FLUIDÃO",
            "CALÇA TRANQUILONA",
            "PANTALONA PAH",
            "BLUSA BÁSICA EU?!",
            "BLUSA FELIZONA",
            "CALÇA FACINHA",
            "CALÇA TECH",
            "MACACÃO MUDÉRNO",
            "SAIA PROTAGONISTA",
            "SAIA ÚNICA",
            "TRENCH FÁCIL",
            "VESTIDO PAH",
            "BOLSA CEO",
            "BOLSA PASSEADEIRA",
            "BOLSA TÔ PRONTA",
            "CLUTCH MODERNOSA",
            "CLUTCH RESORT",
            "BLUSA ACINTURANTE",
            "BLUSA MODERNOSA",
            "CALÇA FESTEIRA",
            "MACACÃO PRA FRENTEX",
            "SAIA BACANUDA",
            "SAIA DELICIA",
            "SAIA DO ÓBVIO",
            "VESTIDO INVERNAL",
            "VESTIDO TÔ PLENA",
            "VESTIDO URBANÓIDE",
            "BOLSA ANDA SOZINHA",
            "BOLSA CLARONA",
            "BOLSA DIA E NOITE",
            "BOLSA MOLONA",
            "BOLSA VIAJANTE",
            "BLUSA GALERISTA",
            "BLUSA MODERNETY",
            "BLUSA NA ESTICA",
            "VESTIDO ESCULTURAL",
            "BLUSA PAH",
            "BLUSA PHYNA",
            "A BOTA PRETA",
            "BRINCO DECÔ",
            "BRINCO CHIQUETÊ",
            "BRINCO PRONTÍSSIMA",
            "SANDÁLIA ARTSY",
            "SANDÁLIA CURINGASSA",
            "RASTEIRA PAH",
            "SANDÁLIA GALERISTA",
            "SANDÁLIA MINIMAL",
            "BLUSA ALONGADORA",
            "CALÇA DIFERENTEX",
            "CAMISA FRESQUINHA",
            "CAMISA RELAX",
            "CAMISA TÔ CHIC",
            "A CAMISA BRANCA",
            "SAIA ANO TODO",
            "TRICÔ ENFEITANTE",
            "VESTIDO DOIS EM UM",
            "VESTIDO OLHA ELA",
            "CALÇA ACINTURANTE",
            "CALÇA FRESQUINHA",
            "CALÇA RELAX",
            "JAQUETA BACANUDA",
            "JAQUETA FRESQUINHA",
            "JAQUETA RELAX",
            "JEANS ANDA SOZINHO",
            "JEANS GOSTOSÃO",
            "SANDÁLIA PODEROSONA",
            "A JAQUETA JEANS",
            "CAMISA VIAJANTE",
            "CAMISA JAQUETOSA",
            "BERMUDA VIAJANTE",
            "MACACÃO COOL",
            "VESTIDO DANÇANTE",
            "A GLADIADORA FENDI",
            "A GLADIADORA PRETA",
            "SANDÁLIA WOW CARAMELO",
            "SANDÁLIA WOW PRETA",
            "BLUSA MINIMAL",
            "CAMISA DE RESPONSA",
            "JAQUETA CHEGUEI",
            "JAQUETA LEVISSIMA",
            "SAIA LEVISSIMA",
            "BODY ARRUMADÃO",
            "BODY CLASSUDÃO",
            "BODY COMBINANTE",
            "BODY MODERNOSO",
            "BODY SEGUNDA PELE",
            "BODY CHIQUERIA",
            "BRINCO FESTEIRO",
            "BRINCO ILUMINADOR",
            "BRINCO PAH",
            "CHOKER MALEÁVEL",
            "COLAR SURPRESA",
            "A CAMISA AZUL",
            "BLUSA BRILHEI",
            "CALÇA TODO DIA",
            "MACACÃO ARTÍSTICO",
            "REGATA WOW",
            "VESTIDO CLEANZÃO",
            "O TRICOZÃO",
            "REGATA CHIQUETOSA",
            "TRICÔ BASIQUETY",
            "TRICOT ANIMADOR",
            "TRICOT DELÍCIA",
            "TRICOT GLAM",
            "TRICOT GOLONA",
            "BRACELETE LEVINHO",
            "BRACELETE PODEROSÃO",
            "BRINCO CHIQUERIA",
            "BRINCO DANÇANTE",
            "COLAR RESOLVEDOR",
        ]


class Saudacao(Intent):
    def __init__(self):
        super().__init__(self.greet())

    def greet(self):
        greetings = [
            "Oi! Tudo bem? Aqui é do time Curadobia ✨ Como posso te ajudar hoje?"
        ]
        greetings.append(self.greet_time())
        others = [
            f"Olá, {self.get_name()}, como posso ajudar você hoje?",
            f"Oi, {self.get_name()}! Em que posso ajudar?",
            f"Oi, {self.get_name()}! Como posso ajudar você hoje?",
            f"Olá, {self.get_name()}! Que bom ver você por aqui.",
        ]
        greetings.extend(others)
        return random.choice(greetings)

    def greet_time(self):
        from datetime import datetime

        current_hour = datetime.now().hour
        if 5 <= current_hour < 12:
            return "Bom dia! Como posso ajudar você hoje?"
        elif 12 <= current_hour < 18:
            return "Boa tarde! Em que posso ajudar?"
        else:
            return "Boa noite! Como posso ajudar você?"


class DuvidaProduto(Intent):
    use_rag = True
    rag_context = "Contexto: Responda dúvidas detalhadas sobre produtos do catálogo da Curadobia, incluindo preço, disponibilidade, tamanhos, materiais e cores."

    def __init__(self):
        super().__init__(self.get_response())

    def get_response(self):
        responses = [
            self.price_doubt(),
            self.stock_doubt(),
            self.size_doubt(),
            self.material_doubt(),
            self.color_doubt(),
        ]
        return random.choice(responses)

    def price_doubt(self):
        products = self.get_products()
        price = random.randint(300, 1000)
        product = random.choice(products)
        return f"O preço do {product} é R$ {price},00."

    def stock_doubt(self):
        products = self.get_products()
        product = random.choice(products)
        availability = random.choice(["disponível", "indisponível"])
        return f"O {product} está atualmente {availability} em nosso estoque."

    def size_doubt(self):
        products = self.get_products()
        product = random.choice(products)
        sizes = ["P", "M", "G", "GG", "36", "38", "40", "42", "44"]
        available_sizes = random.sample(sizes, k=random.randint(1, len(sizes)))
        return (
            f"O {product} está disponível nos tamanhos: {', '.join(available_sizes)}."
        )

    def material_doubt(self):
        products = self.get_products()
        product = random.choice(products)
        materials = ["algodão", "poliéster", "viscose", "linho", "seda", "jeans"]
        material = random.choice(materials)
        return f"O {product} é feito de {material}."

    def color_doubt(self):
        products = self.get_products()
        product = random.choice(products)
        colors = [
            "vermelho",
            "azul",
            "verde",
            "preto",
            "branco",
            "amarelo",
            "rosa",
            "cinza",
        ]
        available_colors = random.sample(colors, k=random.randint(1, len(colors)))
        return f"O {product} está disponível nas cores: {', '.join(available_colors)}."

    def smart_fallback(self, user_text: str, *, reason: Optional[str] = None) -> str:
        return (
            "Ainda não encontrei detalhes desse item no catálogo. Você pode me mandar o nome completo "
            "ou alguma característica? Se preferir, posso passar seu pedido para alguém do time procurar para você."
        )


class SolicitaçãoInformação(Intent):
    use_rag = True
    rag_context = "Contexto: Forneça informações gerais sobre a marca Curadobia, políticas, serviços e orientações para clientes em potencial."

    def __init__(self):
        super().__init__(self.get_response())

    def get_response(self):
        responses = [
            "Posso ajudar com informações sobre nossos produtos, políticas de devolução, métodos de pagamento e muito mais. O que você gostaria de saber?",
            "Estou aqui para ajudar! Sobre qual assunto você gostaria de obter informações?",
            "Fique à vontade para perguntar qualquer coisa! Estou aqui para fornecer as informações que você precisa.",
            "Claro! Sobre qual tópico você gostaria de saber mais? Produtos, serviços, políticas?",
        ]
        return random.choice(responses)

    def smart_fallback(self, user_text: str, *, reason: Optional[str] = None) -> str:
        return (
            "Ainda não tenho essa informação exata à mão. Posso encaminhar sua pergunta "
            "para uma pessoa do time ou, se puder trazer mais detalhes, tento buscar de outro jeito."
        )


class ReaçãoEmocional(Intent):
    def __init__(self):
        super().__init__(self.get_response())

    def get_response(self):
        responses = [
            "Fico feliz em saber disso! Se precisar de algo mais, é só avisar.",
            "Que bom que você está satisfeito! Estou aqui para ajudar no que for preciso.",
            "Adoro ouvir isso! Se tiver mais alguma dúvida ou precisar de ajuda, é só falar.",
            "Isso me deixa muito feliz! Conte comigo para o que precisar.",
            "Amei! 💖 Se eu puder ajudar com algo, é só me dizer",
        ]
        return random.choice(responses)


class InteresseProduto(Intent):
    use_rag = True
    rag_context = "Contexto: Apresente recomendações de produtos relevantes, destacando benefícios, combinações e estilos alinhados ao interesse do cliente."

    def __init__(self):
        super().__init__(
            "Fico feliz que você tenha interesse no nosso produto! Posso ajudar com mais alguma coisa?"
        )

    def get_response(self):
        products = self.get_products()
        product = random.choice(products)
        responses = [
            f"Que ótimo que você se interessou pelo {product}! Posso ajudar com mais alguma coisa?",
            f"Fico feliz que você tenha interesse no {product}! Se precisar de mais informações, é só avisar.",
            f"O {product} é realmente incrível! Se quiser saber mais ou precisar de ajuda, estou aqui.",
            f"Adoro quando alguém se interessa pelo {product}! Conte comigo para o que precisar.",
        ]
        return random.choice(responses)

    def smart_fallback(self, user_text: str, *, reason: Optional[str] = None) -> str:
        return (
            "Não encontrei sugestões certeiras agora, mas posso pedir para o time te mandar "
            "algumas indicações personalizadas. Quer que eu faça isso ou prefere me contar um pouco mais do que procura?"
        )


class Agradecimento(Intent):
    def __init__(self):
        super().__init__(self.get_response())

    def get_response(self):
        responses = [
            "Obrigada! Sigo aqui pro que você precisar 💕",
            "Agradeço! Estou à disposição para ajudar no que for necessário 😊",
        ]
        return random.choice(responses)


class RastreamentoPedido(Intent):
    use_rag = True
    rag_context = "Contexto: Informe status de pedidos, etapas de entrega, prazos e atualizações logísticas para compras realizadas na Curadobia."

    def __init__(self):
        super().__init__(self.get_response())

    def get_response(self):
        order_number = f"#{random.randint(1000, 9999)}"
        return self.get_status(order_number)

    def get_status(self, order_number: str):
        statuses = [
            "em processamento",
            "enviado",
            "em trânsito",
            "entregue",
            "aguardando retirada",
        ]
        status = random.choice(statuses)
        return f"O pedido {order_number} está atualmente {status}."

    def smart_fallback(self, user_text: str, *, reason: Optional[str] = None) -> str:
        return (
            "Não consegui acessar o status desse pedido agora. Pode confirmar o número do pedido "
            "ou, se preferir, aciono alguém do time logístico para te retornar rapidinho."
        )


class SolititacaoContato(Intent):
    use_rag = True
    rag_context = "Contexto: Oriente o cliente sobre canais de contato com a Curadobia, horários de atendimento e formas de suporte humano."

    def __init__(self):
        super().__init__(self.get_response())

    def get_response(self):
        contacts = ["telefone", "e-mail", "WhatsApp", "redes sociais"]
        contact = random.choice(contacts)
        return f"Por favor, informe seu {contact} para que possamos entrar em contato com você."

    def smart_fallback(self, user_text: str, *, reason: Optional[str] = None) -> str:
        return (
            "Ainda não encontrei o canal perfeito aqui. Quer me contar o melhor contato para você "
            "ou prefere que eu peça para alguém do time te acionar?"
        )


class MensagemSistema(Intent):
    def __init__(self):
        super().__init__("Mensagem do sistema recebida. Como posso ajudar você?")


class TrocaDevolucao(Intent):
    use_rag = True
    rag_context = "Contexto: Explique políticas de troca e devolução, prazos, condições e passos necessários para o cliente concluir o processo."

    def __init__(self):
        super().__init__(self.get_response())

    def get_response(self):
        responses = [
            "Para iniciar uma troca ou devolução, por favor, forneça o número do pedido e o motivo da solicitação.",
            "Estamos aqui para ajudar com sua troca ou devolução. Por favor, informe o número do pedido e o motivo.",
            "Claro! Para prosseguir com a troca ou devolução, precisamos do número do pedido e do motivo da solicitação.",
            "Fique tranquilo! Para facilitar sua troca ou devolução, por favor, envie o número do pedido e o motivo.",
        ]
        return random.choice(responses)

    def smart_fallback(self, user_text: str, *, reason: Optional[str] = None) -> str:
        return (
            "Não achei aqui os detalhes da sua troca ou devolução. Pode me enviar o número do pedido "
            "ou quer que eu encaminhe essa solicitação direto para o nosso time especialista?"
        )


class ProblemaTecnico(Intent):
    use_rag = True
    rag_context = "Contexto: Auxilie na resolução de problemas técnicos com o site ou aplicativo, sugerindo passos de solução ou escalonamento para suporte."

    def __init__(self):
        super().__init__(self.get_response())

    def get_response(self):
        responses = [
            "Sinto muito por ouvir isso. Por favor, descreva o problema técnico que você está enfrentando.",
            "Lamento pelo inconveniente. Poderia fornecer mais detalhes sobre o problema técnico?",
            "Entendo que isso pode ser frustrante. Por favor, explique o problema técnico para que possamos ajudar.",
            "Estamos aqui para ajudar! Por favor, informe mais sobre o problema técnico que você está enfrentando.",
        ]
        return random.choice(responses)

    def smart_fallback(self, user_text: str, *, reason: Optional[str] = None) -> str:
        return (
            "Ainda não identifiquei uma solução certeira. Pode compartilhar mais detalhes (como prints ou mensagens "
            "de erro) ou prefere que eu acione o suporte técnico humano para te ajudar?"
        )


class NaoIdentificado(Intent):
    def __init__(self):
        super().__init__(self.get_response())

    def get_response(self):
        responses = [
            "Desculpe, não entendi sua solicitação. Pode reformular?",
            "Não consegui compreender sua mensagem. Poderia explicar de outra forma?",
            "Estou tendo dificuldade em entender. Você poderia tentar dizer isso de outra maneira?",
            "Não tenho certeza do que você quis dizer. Poderia esclarecer?",
        ]
        return random.choice(responses)


class ReposicaoEstoque(Intent):
    use_rag = True
    rag_context = "Contexto: Informe sobre reposição de estoque, alertas de disponibilidade e alternativas quando um item estiver esgotado."

    def __init__(self):
        super().__init__(self.get_response())

    def get_response(self):
        responses = [
            "Obrigado pelo interesse! Estamos trabalhando para repor o estoque o mais rápido possível.",
            "Agradecemos sua paciência. A reposição do estoque está em andamento e em breve os produtos estarão disponíveis novamente.",
            "Ficamos felizes com seu interesse! A reposição do estoque está prevista para breve. Fique atento às novidades.",
            "Obrigado por nos avisar! Estamos agilizando a reposição do estoque para atender à demanda.",
        ]
        return random.choice(responses)

    def smart_fallback(self, user_text: str, *, reason: Optional[str] = None) -> str:
        return (
            "Ainda não temos a data de reposição desse item. Posso anotar seus dados para te avisar assim que chegar "
            "ou prefere que alguém do time comercial entre em contato?"
        )


class Confirmacao(Intent):
    def __init__(self):
        super().__init__(self.get_response())

    def get_response(self):
        responses = [
            "Obrigado pela confirmação! Se precisar de mais alguma coisa, é só avisar.",
            "Agradeço por confirmar! Estou à disposição para ajudar no que for necessário.",
            "Ótimo, obrigado pela confirmação! Se surgir qualquer outra dúvida, estarei por aqui.",
            "Perfeito, obrigado por confirmar! Conte comigo para o que precisar.",
            "Perfeito! Vou seguir com isso pra você. Qualquer coisa, me chama 😊",
        ]
        return random.choice(responses)


class ParceriaComercial(Intent):
    use_rag = True
    rag_context = "Contexto: Descreva possibilidades de parcerias comerciais, requisitos, canais de contato e próximos passos para empresas interessadas."

    def __init__(self):
        super().__init__(self.get_response())

    def get_response(self):
        responses = [
            "Agradecemos seu interesse em uma parceria comercial. Por favor, envie mais detalhes sobre sua proposta.",
            "Ficamos felizes com seu interesse em colaborar conosco! Poderia fornecer mais informações sobre a parceria que você tem em mente?",
            "Obrigado por considerar uma parceria comercial conosco! Estamos ansiosos para saber mais sobre sua proposta.",
            "Agradecemos por pensar em nós para uma parceria comercial. Por favor, compartilhe mais detalhes para que possamos avaliar.",
        ]
        return random.choice(responses)

    def smart_fallback(self, user_text: str, *, reason: Optional[str] = None) -> str:
        return (
            "Ainda não encontrei informações completas sobre parcerias para esse perfil. "
            "Posso direcionar sua proposta para o time comercial analisar ou você pode me passar mais detalhes agora."
        )


class EventoPresencial(Intent):
    use_rag = True
    rag_context = "Contexto: Informe sobre eventos presenciais, agendas, inscrições, locais e experiências oferecidas pela Curadobia."

    def __init__(self):
        super().__init__(self.get_response())

    def get_response(self):
        responses = [
            "Ficamos felizes com seu interesse em nosso evento presencial! Em breve entraremos em contato com mais informações.",
            "Obrigado por se interessar pelo nosso evento presencial! Estamos preparando tudo para que seja uma experiência incrível.",
            "Agradecemos seu interesse em participar do nosso evento presencial! Fique atento às nossas comunicações para mais detalhes.",
            "É ótimo saber que você está interessado no nosso evento presencial! Em breve compartilharemos mais informações.",
        ]
        return random.choice(responses)

    def smart_fallback(self, user_text: str, *, reason: Optional[str] = None) -> str:
        return (
            "A agenda do evento ainda não está disponível aqui. Posso pedir para alguém do time te enviar os detalhes "
            "assim que abrirmos as inscrições ou você prefere deixar mais informações agora?"
        )
