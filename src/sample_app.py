import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    print("Hello from mlflow-jupyter!")
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


if __name__ == "__main__":
    main()
