from utils.file_parser import parse_file

class IngestionAgent:
    def ingest(self, file):
        # Call the parser and return cleaned text chunks
        chunks = parse_file(file)
        return chunks
