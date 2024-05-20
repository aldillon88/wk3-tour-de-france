import re


def remove_whitespace_from_column_names(df):
  # Remove leading and trailing spaces from column names
  df2 = df.copy()
  df2.columns = [column.strip() for column in df2.columns]
  return df2


def trim_and_lower_strings(df):
  df2 = df.copy()
  # Use applymap() with a lambda function to trim and lower strings in all columns
  df2 = df2.apply(lambda x: x.strip() if isinstance(x, str) else x)
  df2 = df2.apply(lambda x: x.lower() if isinstance(x, str) else x)
  return df2


def trim_and_lower(df):
  df2 = df.copy()

  df2.columns = [column.strip() for column in df2.columns]
  df2.columns = [column.strip().replace(" ", "_").lower() for column in df2.columns]

  df2 = df2.map(lambda x: x.strip() if isinstance(x, str) else x)
  df2 = df2.map(lambda x: x.lower() if isinstance(x, str) else x)

  return df2


def extract_string_in_parentheses(text):
  # Define a regular expression pattern to match strings inside parentheses
  pattern = r'\((.*?)\)'
  
  # Use re.findall to find all matches of the pattern in the text
  matches = re.findall(pattern, text)
    
  # If matches are found, return the first match (string inside parentheses)
  # Otherwise, return None
  if matches:
    return matches[0]
  else:
    return "unknown"


def drop_non_numbers(string):
    numbers_str = re.sub(r'[^\d.]', '', string)
    number = round(float("".join(numbers_str)), 2)
    return number


