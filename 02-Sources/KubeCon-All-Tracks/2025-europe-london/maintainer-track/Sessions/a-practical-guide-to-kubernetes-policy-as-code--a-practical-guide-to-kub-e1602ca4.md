---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Kubernetes Core", "Community Governance"]
speakers: ["Jim Bugwadia", "Nirmata", "Rita Zhang", "Microsoft", "Andy Suderman", "Fairwinds", "Joe Betz", "Google"]
sched_url: https://kccnceu2025.sched.com/event/1tcxh/a-practical-guide-to-kubernetes-policy-as-code-jim-bugwadia-nirmata-rita-zhang-microsoft-andy-suderman-fairwinds-joe-betz-google
youtube_search_url: https://www.youtube.com/results?search_query=A+Practical+Guide+To+Kubernetes+Policy+as+Code+CNCF+KubeCon+2025
slides: []
status: parsed
---

# A Practical Guide To Kubernetes Policy as Code - Jim Bugwadia, Nirmata; Rita Zhang, Microsoft; Andy Suderman, Fairwinds; Joe Betz, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Jim Bugwadia, Nirmata, Rita Zhang, Microsoft, Andy Suderman, Fairwinds, Joe Betz, Google
- Schedule: https://kccnceu2025.sched.com/event/1tcxh/a-practical-guide-to-kubernetes-policy-as-code-jim-bugwadia-nirmata-rita-zhang-microsoft-andy-suderman-fairwinds-joe-betz-google
- Busca YouTube: https://www.youtube.com/results?search_query=A+Practical+Guide+To+Kubernetes+Policy+as+Code+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre A Practical Guide To Kubernetes Policy as Code.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcxh/a-practical-guide-to-kubernetes-policy-as-code-jim-bugwadia-nirmata-rita-zhang-microsoft-andy-suderman-fairwinds-joe-betz-google
- YouTube search: https://www.youtube.com/results?search_query=A+Practical+Guide+To+Kubernetes+Policy+as+Code+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=w1wh9dc6m34
- YouTube title: A Practical Guide To Kubernetes Policy as Code - Jim Bugwadia, Rita Zhang, Andy Suderman & Joe Betz
- Match score: 0.742
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/a-practical-guide-to-kubernetes-policy-as-code/w1wh9dc6m34.txt
- Transcript chars: 28118
- Keywords: policy, policies, validating, admission, gatekeeper, actually, kivero, write, cluster, resources, features, validation, mutating, called, resource, within, mutation, working

### Resumo baseado na transcript

I'm joined here by Joe Betts, a staff engineer at Google, who is the SIG API machinery lead. and the founder and CEO of Nurmada, Jim Buguia, who is a co-chair of the policy working group with me and a maintainer of Caverno. probably missed six different projects again we don't have time to cover all of those today so instead I'm going to hand it off to Joe who's going to talk about I'm going to talk about policy within Kubernetes thank you Andy Um so within Kubernetes um policy has been kind of available since about the8 release when we introduced um admission web hooks and this was kind of the foundational extension point that you could use. Is it going to scale to the needs of all the clusters it's installed in? um all the things monitoring everything that comes along with with having a critical component and what we saw in the ecosystem since 18 which is a long time ago is um there's been a lot of problems with admission web hooks in clusters I've

### Excerpt da transcript

All right. Hello everybody. Welcome to a practical guide to Kubernetes policy as code. I'm gonna skip the agenda. You'll see it. It's coming. I'm Andy Sudterman. I'm the CTO of Fairwinds. I'm also a uh co-chair of the policy working group. I'm joined here by Joe Betts, a staff engineer at Google, who is the SIG API machinery lead. Rita Zang, principal engineer at Microsoft, who is the chair of SIG O. and the founder and CEO of Nurmada, Jim Buguia, who is a co-chair of the policy working group with me and a maintainer of Caverno. We're here to talk about policy and policy is code. So, first of all, why should we care about policy? This is a very simple graph from one of the white papers that the policy working group has put out, but basically what we're trying to say here is that policy underpins just about everything that you might care about in your Kubernetes cluster. We're going to talk a little bit more about that and then dive into some specific examples of different policies. Um, recently, uh, Jimmy Ray, another member of the policy working group, wrote a book called policy is code.

We say he wrote the book these days. Um, and he said it is the use of code artifacts to manage and apply rules and conditions. It's a pretty simple definition. I think we can all wrap our heads around that. But if you look across the Kubernetes codebase, you'll see that there's policy in many, many different parts of the codebase. Arbback is policy. We have validating and uh admission policies. We have ON and OZ which are types of policies. We have network policy. We have cublet configurations. We have quotas, limit ranges, resource quotas. We have all these different things that are policy. Um we don't have time in 30 minutes to cover all of those today. So we're just going to cover a small portion of those uh in the next few minutes. But why should we do policy as code? Why shouldn't we run individual programs to enforce policy? Um, and really it's just all the reasons that we care about doing things as code. It's very similar to infrastructure as code. It's more maintainable. It's more efficient. We can uh all inspect it together.

We can do code review on it. We can see how uh policy uh is working within our system. Uh and Kubernetes provides a lot of different patterns for this. uh we have policy enforcement points already built into the code everywhere. So uh with that I am going to oh apologies one more uh quick disclaimer again we're not going to cover all the di
