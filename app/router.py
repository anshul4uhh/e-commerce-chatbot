from semantic_router import Route
from semantic_router.routers import SemanticRouter

from semantic_router.encoders import HuggingFaceEncoder

encoder = HuggingFaceEncoder(
    name="sentence-transformers/all-MiniLM-L6-v2"
)

faq = Route(
    name='faq',
    utterances=[
        "What is the return policy of the products?",
        "What is your policy for damaged or defective products?",
        "What should I do if I receive a damaged item?",
        "How can I get a replacement for a broken product?",
        "Do I get a discount with the HDFC credit card?",
        "How can I track my order?",
        "What payment methods are accepted?",
        "Is debit card payment accepted?",
        "Can I pay using my debit card?",
        "What are the available payment options?",
        "Do you support UPI, credit card, and debit card?",
        "How long does it take to process a refund?",
        "Is there any warranty on the products?",
        "How do I cancel my order?",
        "is cash on delivery payment method accecpted?",
        "Do you provide international shipping?",
        "Can I change my delivery address after ordering?",
        "How can I contact customer support?",
        "what's ur refund policy?"
    ]
)


sql = Route(
    name='sql',
    utterances=[
        "I want to buy Nike shoes that have a 50% discount.",
        "Are there any shoes under Rs. 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        "What is the price of Puma running shoes?",
        "Show me men's sports shoes between 2000 and 4000.",
        "Do you have black sneakers for men?",
        "List Adidas shoes available in size 8.",
        "Which shoes are trending right now?",
        "Show me all footwear with customer rating above 4."
    ]
)

routes = [faq,sql]
router = SemanticRouter(encoder=encoder,routes=routes,auto_sync="local")

if __name__=="__main__":
    print(router("is cash on delivery payment method accecpted?").name)
    print(router("show me black sneakers").name)