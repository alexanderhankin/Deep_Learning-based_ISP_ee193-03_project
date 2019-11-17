function metadata = load_metadata(data_path)
  f = fopen(data_path);
  metadata = (textscan(f, '%q %q', 'Delimiter', ','));
  fclose(f);
end
