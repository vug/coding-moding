# Generalizations vs specializations

https://leetcode.com/problems/defanging-an-ip-address/

Generalization is to write replace all [std::basic\_string<CharT,Traits,Allocator>::replace \- cppreference\.com](https://en.cppreference.com/w/cpp/string/basic_string/replace)

But optimized solution uses the fact that the input is a valid IP address. So, after defanging, there can be at most `4*3 + 3*3 = 21` characters. 

Can do with strings. Probably fastest is to use array of chars.

Looks like `string` and `vector` have very similar API. `resize`, `reserve`, `size`, `push_back` etc.

## References

* [std::basic\_string \- cppreference\.com](https://en.cppreference.com/w/cpp/string/basic_string)
  * [std::basic\_string<CharT,Traits,Allocator>::basic\_string \- cppreference\.com](https://en.cppreference.com/w/cpp/string/basic_string/basic_string)
  * [std::basic\_string<CharT,Traits,Allocator>::replace \- cppreference\.com](https://en.cppreference.com/w/cpp/string/basic_string/replace)
  * [std::basic\_string<CharT,Traits,Allocator>::reserve \- cppreference\.com](https://en.cppreference.com/w/cpp/string/basic_string/reserve)
  * [std::basic\_string<CharT,Traits,Allocator>::resize \- cppreference\.com](https://en.cppreference.com/w/cpp/string/basic_string/resize)