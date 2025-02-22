# Output:
![image](https://github.com/user-attachments/assets/2396a110-8307-42a7-9614-6c268e9e2ea5)

# Comparison:
# 🛣️ Romania Map Search Algorithms Comparison

This table compares different search algorithms for finding the shortest path in the Romania road map problem.

| Algorithm                    | Completeness | Optimality | Time Complexity (Big-O) |
|------------------------------|-------------|------------|--------------------------|
| **Breadth-First Search (BFS)** | ✅ Yes      | ❌ No      | O(b^d) (Exponential)     |
| **Uniform Cost Search (UCS)** | ✅ Yes      | ✅ Yes     | O(b^d) (Exponential)     |
| **Greedy Best-First Search**  | ✅ Yes      | ❌ No      | O(b^m) (Worst Case)      |
| **Iterative Deepening DFS**   | ✅ Yes      | ❌ No      | O(b^d) (Exponential)     |

### 📌 **Key:**
- ✅ **Completeness** → The algorithm always finds a solution if one exists.
- ✅ **Optimality** → The algorithm guarantees the shortest path.
- **b** = branching factor, **d** = depth of the shallowest goal, **m** = maximum depth.

🚀 **Conclusion:**
- **UCS is the best choice if you want the shortest path.**  
- **Greedy Best-First Search is faster but doesn't guarantee the best path.**  
- **BFS & IDDFS are not optimal but work well for simple problems.**  
