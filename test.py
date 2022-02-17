import pickle

def main():
	pickle.loads(open("/tmp/pickle_fn", "rb").read())()

if __name__ == "__main__":
	main()
