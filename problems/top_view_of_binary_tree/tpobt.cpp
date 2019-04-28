// g++ tpobt.cpp --std=c++11
#include <iostream>
#include <stdio.h>
#include <tuple>
#include <unordered_map>
#include <vector>

using namespace std;

class Node
{
  public:
    int val;
    Node *left;
    Node *right;

    Node(int val)
    {
        this->val = val;
        this->right = NULL;
        this->left = NULL;
    }
};

void print_tree(Node *node, int depth = 0)
{
    if (node == NULL)
    {
        return;
    }
    for (int i = 0; i < depth; i++)
    {
        cout << " ";
    }
    cout << node->val << endl;

    print_tree(node->left, depth + 1);
    print_tree(node->right, depth + 1);
}

unordered_map<int, tuple<int, Node *>> tops;

void print_tops()
{
    cout << "tops: ";
    for (auto &i : tops)
    {
        cout << i.first << ":" << get<1>(i.second)->val << ",";
    }
    cout << endl;
}

void traverse(Node *root, int x, int y)
{
    if (root == NULL)
        return;

    if (tops.find(x) == tops.end() || y < get<0>(tops[x]))
    {
        tops[x] = make_tuple(y, root);
    }
    traverse(root->left, x - 1, y + 1);
    traverse(root->right, x + 1, y + 1);
}

vector<int> top_view(Node *root)
{
    traverse(root, 0, 0);

    // sort x coords
    vector<int> xs;
    for (auto &i : tops)
    {
        xs.push_back(i.first);
    }
    sort(xs.begin(), xs.end());

    // get top view values sorted by x-axis
    vector<int> result;
    for (auto &i : xs)
    {
        result.push_back(get<1>(tops[i])->val);
    }

    return result;
}

int main()
{
    Node *root = new Node(5);
    root->left = new Node(3);
    root->left->left = new Node(1);
    root->left->right = new Node(4);
    root->right = new Node(10);
    root->right->left = new Node(7);

    auto result = top_view(root);
    for (auto &i : result)
    {
        cout << i << " ";
    }
    cout << endl;
}
