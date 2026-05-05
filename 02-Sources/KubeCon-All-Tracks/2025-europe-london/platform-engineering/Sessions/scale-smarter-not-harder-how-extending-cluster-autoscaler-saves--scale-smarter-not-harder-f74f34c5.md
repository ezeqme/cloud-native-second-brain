---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["Platform Engineering", "Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Rahul Rangith", "Ben Hinthorne", "Datadog"]
sched_url: https://kccnceu2025.sched.com/event/1txA8/scale-smarter-not-harder-how-extending-cluster-autoscaler-saves-millions-rahul-rangith-ben-hinthorne-datadog
youtube_search_url: https://www.youtube.com/results?search_query=Scale+Smarter+Not+Harder%3A+How+Extending+Cluster+Autoscaler+Saves+Millions+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Scale Smarter Not Harder: How Extending Cluster Autoscaler Saves Millions - Rahul Rangith & Ben Hinthorne, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Rahul Rangith, Ben Hinthorne, Datadog
- Schedule: https://kccnceu2025.sched.com/event/1txA8/scale-smarter-not-harder-how-extending-cluster-autoscaler-saves-millions-rahul-rangith-ben-hinthorne-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=Scale+Smarter+Not+Harder%3A+How+Extending+Cluster+Autoscaler+Saves+Millions+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Scale Smarter Not Harder: How Extending Cluster Autoscaler Saves Millions.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txA8/scale-smarter-not-harder-how-extending-cluster-autoscaler-saves-millions-rahul-rangith-ben-hinthorne-datadog
- YouTube search: https://www.youtube.com/results?search_query=Scale+Smarter+Not+Harder%3A+How+Extending+Cluster+Autoscaler+Saves+Millions+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=CQ3Wxg4qNaQ
- YouTube title: Scale Smarter Not Harder: How Extending Cluster Autoscaler Saves Mi... Rahul Rangith & Ben Hinthorne
- Match score: 0.923
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/scale-smarter-not-harder-how-extending-cluster-autoscaler-saves-millio/CQ3Wxg4qNaQ.txt
- Transcript chars: 27665
- Keywords: instance, cluster, autoscaler, expander, clusters, cost, another, across, groups, groupoup, application, performance, applications, running, optimal, within, packing, memory

### Resumo baseado na transcript

My name is Ben and I'm here with my colleague Rahul and we are both software engineers at data dog. So we're going to start today by talking a little bit about how we do node autoscaling at data dog. If you're familiar with the cluster autoscaler, you might be familiar with their concept of a node group and ours is similar. And for the sake of time, I won't get into too much detail about why we use the cluster autoscaler over other autoscaling alternatives. But at a high level, one of the main reasons we use cluster autoscaler is because it has support for all the cloud providers that we need within our infrastructure as well. We've been running cluster autoscaler for a while now and we're happy with the operational experience we've been having in our clusters and have been able to contribute upstream with features when we need them.

### Excerpt da transcript

Hi everyone. Thank you all for coming to our talk today. Uh our talk is called scaling smarter not harder. How extending cluster autoscaler saves millions. My name is Ben and I'm here with my colleague Rahul and we are both software engineers at data dog. So we're going to start today by talking a little bit about how we do node autoscaling at data dog. before diving into the cluster autoscaler and the concept of expanders and then we're going to move into talking about how we identify optimal instance types and then how we scale those optimal instance types. So first a bit about data dog. We run Kubernetes from scratch in a multi cloud environment. We run across dozens of clusters with tens of thousands of nodes and hundreds of thousands of pods. And within this infrastructure, we serve trillions of data points per hour for over 30,000 customers. At Data Dog, Rahul and I both work on a team called compute autoscaling. At a high level, the goal of our team is to manage the node infrastructure for product teams to enable product teams to focus on product development while we focus on the node infrastructure.

In doing so, we focus on things like scheduling and scaling efficiency to deliver nodes as fast as possible as well as binacking and cost optimizations across our fleet. So, a key offering of our platform is something that we call a node group set. So, first a node group we can think of as a cloud provider agnostic representation for something like an autoscaling group or a manage instance group. If you're familiar with the cluster autoscaler, you might be familiar with their concept of a node group and ours is similar. But we have a custom resource definition defined in our environment that we use for node groupoups. We have one more abstraction on top of a node group which we call a node groupoup set. A node groupoup set is a set of node groupoups that falls under the same scheduling domain. So what that means if an application specifies a toleration or a node affinity for our node groupoup set then they could schedule onto any of the underlying node groups that would fit their pod. So node groupoup sets are beneficial for us for a few reasons.

One of them is it makes it a lot easier for us to onboard and manage many users and many applications across data dog because they can just set the specification for the node group set and then we can change out the underlying node groups or instance types beneath them without them changing anything else on t
