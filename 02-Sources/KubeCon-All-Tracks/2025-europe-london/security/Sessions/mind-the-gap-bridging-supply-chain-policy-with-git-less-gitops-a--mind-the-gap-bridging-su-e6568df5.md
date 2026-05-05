---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Security"
themes: ["AI ML", "Security", "GitOps Delivery"]
speakers: ["Michael Lieberman", "Kusari", "Andrew Martin", "ControlPlane"]
sched_url: https://kccnceu2025.sched.com/event/1tx8R/mind-the-gap-bridging-supply-chain-policy-with-git-less-gitops-and-guac-michael-lieberman-kusari-andrew-martin-controlplane
youtube_search_url: https://www.youtube.com/results?search_query=Mind+the+Gap%3A+Bridging+Supply+Chain+Policy+With+Git-less+GitOps+and+GUAC+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Mind the Gap: Bridging Supply Chain Policy With Git-less GitOps and GUAC - Michael Lieberman, Kusari & Andrew Martin, ControlPlane

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[GitOps Delivery]]
- País/cidade: United Kingdom / London
- Speakers: Michael Lieberman, Kusari, Andrew Martin, ControlPlane
- Schedule: https://kccnceu2025.sched.com/event/1tx8R/mind-the-gap-bridging-supply-chain-policy-with-git-less-gitops-and-guac-michael-lieberman-kusari-andrew-martin-controlplane
- Busca YouTube: https://www.youtube.com/results?search_query=Mind+the+Gap%3A+Bridging+Supply+Chain+Policy+With+Git-less+GitOps+and+GUAC+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Mind the Gap: Bridging Supply Chain Policy With Git-less GitOps and GUAC.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx8R/mind-the-gap-bridging-supply-chain-policy-with-git-less-gitops-and-guac-michael-lieberman-kusari-andrew-martin-controlplane
- YouTube search: https://www.youtube.com/results?search_query=Mind+the+Gap%3A+Bridging+Supply+Chain+Policy+With+Git-less+GitOps+and+GUAC+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=D21yF0E-v2s
- YouTube title: Mind the Gap: Bridging Supply Chain Policy With Git-less GitOps... Michael Lieberman & Andrew Martin
- Match score: 0.904
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/mind-the-gap-bridging-supply-chain-policy-with-git-less-gitops-and-gua/D21yF0E-v2s.txt
- Transcript chars: 27491
- Keywords: software, security, source, supply, vulnerability, cluster, actually, running, somebody, foundation, projects, systems, sbombs, control, artifact, flux, production, information

### Resumo baseado na transcript

Welcome to Mind the Gap, the the most uh British pun we could attempt for the talk content. Uh despite the shaky start, I am in fact CEO at control plane, co-chair in tag security in years gone by that is now an emeritus position and CISO at open UK where we focus on open source, open hardware and open data and attempting So security will always be one step behind and organizations that hyper prioritize security above features are doomed to deliver features more slowly. That's what we're seeing across supply chain security at large and the CRA by trying to deal with the fact that botn nets based in light bulbs took down MK for a multi-billion dollar insurance claim and wiped out physical supply chains. So, as we've said, security will always sit one step behind feature delivery. This is about as far as we'll go with the context framing of the problem.

### Excerpt da transcript

Very good afternoon everybody. Welcome to Mind the Gap, the the most uh British pun we could attempt for the talk content. Bridging supply chain policy with Gitless, GitOps, and Guac. I'm Andy. Uh Clicker is here. Let's move that out slightly. And it's not quite working. You're focused on the wrong thing. Yeah, thank you. Thank you. There we go. Hello. Uh despite the shaky start, I am in fact CEO at control plane, co-chair in tag security in years gone by that is now an emeritus position and CISO at open UK where we focus on open source, open hardware and open data and attempting to prevent regulatory bodies and governments from blowing their own feet off with things like the CRA, which we'll talk about more. And this is my dear friend. Hi, I'm uh Mike Lieberman. I'm co-founder and CTO of Cusari. Uh done a whole bunch of stuff in open source. Uh am a tech lead in tag security. I'm a governing board member of the open source security foundation or open SSF as well as a TAC member and a maintainer of various open source projects like GU and Salsa.

And also there's a book that if uh folks are interested, right? So what are we going to talk about today? You may have heard of the cyber resilience act that we'll feature intermittently throughout GUAC the graph for understanding artifact composition and how to manage CVS where that is relevant to GitOps flux declarative paradigms and ultimately security a live demo which I hope you're as excited about as I am and then how do we tighten that even further with the things that wouldn't fit into a half hour talk and then some of the extra things that we can see around Timony and Q on the edge of the ecosystem. So uh the cyber resilience act uh okay so not going to go too deep into this but what is it right so uh a lot of folks who are selling in Europe you're now responsible for the security of your software that includes what you are pulling in that means uh no more blaming open source for the problem open source is now your problem too so what do we mean right like it's been the same old story every here.

Supply chain attacks, attacks against open source, attacks against vendor software, uh things like you know uh the XZ utils issue from uh last year again uh uh things like the NHS blood tests which were compromised. Um if folks remember polyfill.io IO where somebody had compromised the DNS uh and things like Cisco Duo and uh from Orange Cyber Defense uh there was some research where 58% of all UK financial servi
