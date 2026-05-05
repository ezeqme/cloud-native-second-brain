---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Bill Mulligan", "Paul Arah", "Isovalent @ Cisco", "Neha Aggarwal", "Microsoft", "Satish Krishnan", "UBS"]
sched_url: https://kccncna2025.sched.com/event/27Nnr/10-years-of-cilium-connecting-securing-and-simplifying-the-cloud-native-stack-bill-mulligan-paul-arah-isovalent-cisco-neha-aggarwal-microsoft-satish-krishnan-ubs
youtube_search_url: https://www.youtube.com/results?search_query=10+Years+of+Cilium%3A+Connecting%2C+Securing%2C+and+Simplifying+the+Cloud+Native+Stack+CNCF+KubeCon+2025
slides: []
status: parsed
---

# 10 Years of Cilium: Connecting, Securing, and Simplifying the Cloud Native Stack - Bill Mulligan & Paul Arah, Isovalent @ Cisco; Neha Aggarwal, Microsoft; Satish Krishnan, UBS

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Bill Mulligan, Paul Arah, Isovalent @ Cisco, Neha Aggarwal, Microsoft, Satish Krishnan, UBS
- Schedule: https://kccncna2025.sched.com/event/27Nnr/10-years-of-cilium-connecting-securing-and-simplifying-the-cloud-native-stack-bill-mulligan-paul-arah-isovalent-cisco-neha-aggarwal-microsoft-satish-krishnan-ubs
- Busca YouTube: https://www.youtube.com/results?search_query=10+Years+of+Cilium%3A+Connecting%2C+Securing%2C+and+Simplifying+the+Cloud+Native+Stack+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre 10 Years of Cilium: Connecting, Securing, and Simplifying the Cloud Native Stack.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Nnr/10-years-of-cilium-connecting-securing-and-simplifying-the-cloud-native-stack-bill-mulligan-paul-arah-isovalent-cisco-neha-aggarwal-microsoft-satish-krishnan-ubs
- YouTube search: https://www.youtube.com/results?search_query=10+Years+of+Cilium%3A+Connecting%2C+Securing%2C+and+Simplifying+the+Cloud+Native+Stack+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EN_77SkK5jg
- YouTube title: 10 Years of Cilium: Connecting, Securing, and Simplifying the... Bill M, Paul A, Marcelo M & Neha A
- Match score: 0.887
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/10-years-of-cilium-connecting-securing-and-simplifying-the-cloud-nativ/EN_77SkK5jg.txt
- Transcript chars: 25457
- Keywords: celium, tunnel, security, cluster, workloads, running, psyllium, basically, tetragonon, clusters, actually, network, selium, traffic, single, everyone, observability, support

### Resumo baseado na transcript

So if you aren't sure where you are right now, this is silly maintainers track. But before we kind of dive into the details of this session, I'm going to take you back a decade. It's solving your networking or network policy or network observability challenges, but it's also setting you up for the future too with gateway API multicluster and now MTLS with ingress which we'll also uh with um Zunnel which we'll also hear about later. And then on the security and observability side, it's things around uh DNS host firewall, being able to track trace packets through your network, so you're not stuck uh trying to debug your network at 2 a.m. If you go to the Psyllium website, there's almost a hundred case studies about different companies across every industry, every single challenge, and the things that they've been able to overcome and how they've able been able to improve their business with Psyllium. To give you a perspective on our scale, we're not the biggest well yet, but we are growing every day.

### Excerpt da transcript

Okay, Syllium maintainers track session. Thanks everyone for coming today 10 years. So if you aren't sure where you are right now, this is silly maintainers track. Psyllium is a CNI. It does observability. It does security with Tetreon and all of that is powered by EVPF. But before we kind of dive into the details of this session, I'm going to take you back a decade. So first of all, Selium finally 10 years old. Pretty exciting. And when the project was founded 10 years ago, there was no AI. There's barely containers. There's barely Kubernetes. And so in the past 10 years, obviously, we've seen a massive growth growth in cloud native. And what's kind of happened? So one decade in where are we? Well from that first initial commit that you saw Selenium has grown to community of over a thousand individ individual contributors and in the latest annual report uh the project as a total has almost 50,000 stars on GitHub. Even though even if those are a bit of a vanity metric it's pretty cool to see the community the people and all of you in the room here today too.

But kind of besides those things, what are we actually doing? So in the latest state of Kubernetes networking report, uh we asked people which CNI are you using in your environment and the top result uh with two-thirds of the votes was selium and isalent. I think that's a really good testament to how is really becoming the standard for cloudnative security observability um and networking. Everybody is standardizing on top of selium. And you'll hear later today from some of our end users about that too. And in the same state of Kubernetes networking report, we asked what are you looking at in the next uh 12 months? What kind of issues are you looking at? And people are talking about gateway API multi multicluster connectivity ebpfbased capabilities. And when we looked at the selium user survey, you know, that's exactly what selium has. So choosing Psyllium as a platform for your cloudnative environment is setting you up for today. It's solving your networking or network policy or network observability challenges, but it's also setting you up for the future too with gateway API multicluster and now MTLS with ingress which we'll also uh with um Zunnel which we'll also hear about later.

Selium is also the only graduated project in the CNCF. Even a decade in, it's become the leader in the space. And the innovation doesn't stop. 10 years in, the project continues to lead the way. And so in the latest 1.19
