def param_testing(test_data: dict[str, int], max_value: int) -> tuple[int, int]:
  if 'offset' not in test_data:
    test_data['offset'] = 0
  elif 'limit' not in test_data:
    test_data['limit'] = 10

  end_range = test_data['offset'] + test_data['limit']
  if end_range > max_value:
    end_range = max_value

  return test_data['offset'], end_range