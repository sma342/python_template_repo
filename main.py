import sys
from logic.london_gloom import evaluate_vibe

def main():
    print("=== WELCOME TO THE SHADOW REALM OF BRITAIN ===")
    print("Jesteś edgy? Sprawdźmy to.")
    print("--------------------------------------------")
    
    weather = input("Jaka jest pogoda? (rain / sun / grey): ")
    tea_status = input("Masz herbatę w domu? (jest / none): ")
    
    try:
        pounds = float(input("Ile funtów (£) zostało Ci w kieszeni?: "))
    except ValueError:
        print("Nawet nie umiesz wpisać liczby. To smutne.")
        sys.exit(1)
        
    # Wywołanie logiki
    werdykt = evaluate_vibe(weather, tea_status, pounds)
    
    print("\n[TWÓJ STATUS]:")
    print(werdykt)

if __name__ == "__main__":
    main()