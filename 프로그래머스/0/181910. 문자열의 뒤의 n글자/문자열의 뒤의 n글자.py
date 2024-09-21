def solution(my_string, n):
    m_len = len(my_string) - n
    return my_string[m_len:m_len+n:]