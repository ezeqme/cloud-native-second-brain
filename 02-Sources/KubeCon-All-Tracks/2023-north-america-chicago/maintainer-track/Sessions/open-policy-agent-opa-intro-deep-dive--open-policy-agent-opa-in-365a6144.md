---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Charlie Egan", "Styra", "Sertaç Özercan", "Microsoft"]
sched_url: https://kccncna2023.sched.com/event/1R2uD/open-policy-agent-opa-intro-deep-dive-charlie-egan-styra-sertac-ozercan-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Open+Policy+Agent+%28OPA%29+Intro+%26+Deep+Dive+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Open Policy Agent (OPA) Intro & Deep Dive - Charlie Egan, Styra & Sertaç Özercan, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Charlie Egan, Styra, Sertaç Özercan, Microsoft
- Schedule: https://kccncna2023.sched.com/event/1R2uD/open-policy-agent-opa-intro-deep-dive-charlie-egan-styra-sertac-ozercan-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Open+Policy+Agent+%28OPA%29+Intro+%26+Deep+Dive+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Open Policy Agent (OPA) Intro & Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2uD/open-policy-agent-opa-intro-deep-dive-charlie-egan-styra-sertac-ozercan-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Open+Policy+Agent+%28OPA%29+Intro+%26+Deep+Dive+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XtA-NKoJDaI
- YouTube title: Open Policy Agent (OPA) Intro & Deep Dive - Charlie Egan & Anders Eknert, Styra
- Match score: 0.772
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/open-policy-agent-opa-intro-deep-dive/XtA-NKoJDaI.txt
- Transcript chars: 24364
- Keywords: policy, language, llinter, version, improvements, server, gatekeeper, performance, already, important, talking, course, anders, working, written, provide, another, basically

### Resumo baseado na transcript

So many turned up here uh despite the last being this being the last session. Um we're both open maintainers and uh yeah we're happy to present to you today. And this can be any JSON value rep representing uh an operation which has maybe been taken by a user or a new resource which is looking to land in a Kubernetes cluster. It's also possible to share common security policies that your organization may have between teams. Uh and it allows you to um configure policy controls for Kubernetes admission using custom resources. One problem is that we see a lot and something that people that trips up a lot of people is that uh they have these uh this rule body with all these conditions and they did everything right.

### Excerpt da transcript

Wow, it's great. So many turned up here uh despite the last being this being the last session. So thank you for that. Uh yeah, we're uh we're here to talk about OPA today. Uh are you all familiar with that or show of hands? How many users how many users of OPA do we have here? About half. Cool. Yep. We'll do both an intro and a deep dive. So hopefully there's something for everyone. Yeah. Okay. So do you want to do quick intros? Yeah. Hello everybody. I'm Charlie. I work on the developer relations team at Styra with Anders. Um we're both open maintainers and uh yeah we're happy to present to you today. Thanks for coming out. Yeah, I think you you already I'm Anders and I work in the same team. So, um, yeah, I'd like to start these presentations just to get people thinking about what is policy. I think we've it's a word that people, we're meant to do this to start it off, just get people thinking about what is policy. Everybody's got a different idea about what policy means to them or the first thing that comes into their mind.

But I think for the purposes of this presentation and for thinking about open policy agent, it's important to think about policy as being many different things. um anywhere in your different applications you're working on or platforms you're working with where you need to implement something that looks like a rule whether it's authorizing users granting different tenants in a Kubernetes platform access to do particular things there uh defining custom rules and CI jobs uh implementing business policy and applications all of these things are within scope for what we're talking about today so that's what policy is policyy's rules rules uh and I made reference to various technical policies there but often policy is kind of legal policy or policy that might be written in your employee handbook. Um today we're talking about policy as code. That's what open policy agent is really all about. Um and this is just an example showing you know policy in natural language versus a policy as code. As you can see, it's uh something that you could uh you could write down and express as code.

That's what we're talking about. So, how does how does that's his title. That's a shame. Um how does policy as code work? So, how does OPE work with policy as code? So as a sort of simple model is that you provide some information about a decision that you're interested to make or have OPER make for you and you've preloaded OpE with some uh some policy configura
