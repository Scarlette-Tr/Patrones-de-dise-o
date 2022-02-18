class objetivo:
    
     def request(self) -> str:
        return "objetivo"

class Adaptee:
    def specific_request(self) -> str:
        return "....."

class Adapter(objetivo, Adaptee):
     def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"

def client_code(Objetivo: "objetivo") -> None:
    print(Objetivo.request(), end="")

if __name__ == "__main__":
    print("Client: puede ir trabajando con los objeto objetivo:")
    target = objetivo()
    client_code(objetivo)
    print("\n")

    adaptee = Adaptee()
    print("Cliente: hola, mira estoo")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("ClientE: puede trabajar")
    adapter = Adapter()
    client_code(adapter)