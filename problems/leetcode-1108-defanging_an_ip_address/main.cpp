#include "utils.hpp"

#include <fmt/core.h>

#include <string>

std::string defangIPaddr1(std::string address)
{
    char result[22];
    size_t resIx = 0;
    for (size_t i = 0; i < address.size(); ++i)
    {
        if (address[i] != '.')
        {
            result[resIx++] = address[i];
        }
        else
        {
            result[resIx++] = '[';
            result[resIx++] = '.';
            result[resIx++] = ']';
        }
    }
    result[resIx] = '\0';
    return result;
}

std::string defangIPaddr2(std::string addr) {
    std::string r;
    r.reserve(22); // makes faster
    for (char c : addr) {
        if (c == '.')
            r += "[.]";
        else
            r += c;    
    }
    return r;
}

std::string defangIPaddr3(std::string addr) {
    std::string r;
    r.reserve(21); // doesn't affect much
    for (char c : addr) {
        if (c == '.') {
            r.push_back('[');
            r.push_back('.');
            r.push_back(']');
        }
        else
            r.push_back(c);    
    }
    return r;
}

uint32_t countChar(const std::string &str, char ch)
{
    uint32_t cnt = 0;
    for (char c : str)
        if (c == ch)
            ++cnt;
    return cnt;
}

std::string defangIPaddr4(std::string address)
{
    uint32_t numDots = countChar(address, '.'); // O(N) not needed since IP maximum size is known
    size_t size = address.size() + numDots * 2;
    std::string result(size, ' ');
    size_t resIx = 0;
    for (int i = 0; i < address.size(); ++i)
    {
        if (address[i] != '.')
        {
            result[resIx++] = address[i];
        }
        else
        {
            result[resIx++] = '[';
            result[resIx++] = '.';
            result[resIx++] = ']';
        }
    }
    return result;
}

std::string defangIPaddr4b(std::string address)
{
    std::string result(22, ' ');
    size_t resIx = 0;
    for (int i = 0; i < address.size(); ++i)
    {
        if (address[i] != '.')
        {
            result[resIx++] = address[i];
        }
        else
        {
            result[resIx++] = '[';
            result[resIx++] = '.';
            result[resIx++] = ']';
        }
    }
    result.resize(resIx); // shrinking is not expensive
    return result;
}

int main()
{
    const int count = 10'000'000;
    const std::string ip{"255.100.50.0"};
    Timer t;
    for (int i = 0; i < count; ++i)
        defangIPaddr1(ip); 
    float dur1 = t.timeSinceLastMs();
    for (int i = 0; i < count; ++i)
        defangIPaddr2(ip);
    float dur2 = t.timeSinceLastMs();
    for (int i = 0; i < count; ++i)
        defangIPaddr3(ip);
    float dur3 = t.timeSinceLastMs();
    for (int i = 0; i < count; ++i)
        defangIPaddr4(ip);
    float dur4 = t.timeSinceLastMs();
    for (int i = 0; i < count; ++i)
        defangIPaddr4b(ip);
    float dur4b = t.timeSinceLastMs();

    fmt::print("4b >>>{}<<<\n", defangIPaddr4b(ip));
    fmt::print("dur1 {}, dur2 {}, dur3 {}, dur4 {}, dur4b {}\n", dur1, dur2, dur3, dur4, dur4b);
}