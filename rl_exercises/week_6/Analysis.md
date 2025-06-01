## Analysis of Actor-Critic Baselines (Level 1 – Step 4)

In this part of the assignment, we investigated how different baseline strategies affect the learning performance of an Actor-Critic agent. Specifically, we compared four variants: `none`, `avg`, `value`, and `gae`. Each agent was trained for 200,000 steps on two environments — `CartPole-v1` and `LunarLander-v3` — and we evaluated the average return every 10,000 steps.

### CartPole-v1

Since CartPole is a relatively easy and stable environment, all baseline strategies managed to eventually reach high returns. That said, there were still noticeable differences in stability and learning speed. The `none` baseline showed quite a lot of variance — sometimes it did well, but performance often dropped suddenly. The `avg` baseline was slightly more stable, but still inconsistent.

The best results came from the `value` and `gae` baselines. These approaches led to faster and more reliable learning, with consistently high returns after only a short number of steps. Especially `gae` seemed to combine stable updates with efficient learning.

### LunarLander-v3

This environment was much more challenging. Learning here was slower overall and much more sensitive to the choice of baseline. The `none` and `avg` baselines struggled a lot. Their performance stayed low for a long time and only improved slightly toward the end of training, if at all.

In contrast, the `value` baseline showed a clear improvement over time, even though it started with a big dip in performance. It gradually learned a decent policy and became more stable. The `gae` baseline started off badly as well but recovered in the second half of training. It didn’t fully catch up to `value`, but still outperformed the simpler baselines by a wide margin.