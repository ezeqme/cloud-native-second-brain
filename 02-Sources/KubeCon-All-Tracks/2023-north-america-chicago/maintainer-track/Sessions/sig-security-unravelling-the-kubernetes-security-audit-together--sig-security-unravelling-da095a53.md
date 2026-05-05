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
themes: ["AI ML", "Security", "Kubernetes Core", "Community Governance"]
speakers: ["Rey Lejano", "SUSE", "Savitha Raghunathan", "Red Hat", "Ala Dewberry", "VMware", "Pushkar Joglekar", "Independent"]
sched_url: https://kccncna2023.sched.com/event/1R2mT/sig-security-unravelling-the-kubernetes-security-audit-together-rey-lejano-suse-savitha-raghunathan-red-hat-ala-dewberry-vmware-pushkar-joglekar-independent
youtube_search_url: https://www.youtube.com/results?search_query=SIG+Security%3A+Unravelling+the+Kubernetes+Security+Audit+Together+CNCF+KubeCon+2023
slides: []
status: parsed
---

# SIG Security: Unravelling the Kubernetes Security Audit Together - Rey Lejano, SUSE; Savitha Raghunathan, Red Hat; Ala Dewberry, VMware; Pushkar Joglekar, Independent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Rey Lejano, SUSE, Savitha Raghunathan, Red Hat, Ala Dewberry, VMware, Pushkar Joglekar, Independent
- Schedule: https://kccncna2023.sched.com/event/1R2mT/sig-security-unravelling-the-kubernetes-security-audit-together-rey-lejano-suse-savitha-raghunathan-red-hat-ala-dewberry-vmware-pushkar-joglekar-independent
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+Security%3A+Unravelling+the+Kubernetes+Security+Audit+Together+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre SIG Security: Unravelling the Kubernetes Security Audit Together.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2mT/sig-security-unravelling-the-kubernetes-security-audit-together-rey-lejano-suse-savitha-raghunathan-red-hat-ala-dewberry-vmware-pushkar-joglekar-independent
- YouTube search: https://www.youtube.com/results?search_query=SIG+Security%3A+Unravelling+the+Kubernetes+Security+Audit+Together+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qTKEd8mcb1U
- YouTube title: SIG Security: Unravelling the Kubernetes Security Audit Together
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/sig-security-unravelling-the-kubernetes-security-audit-together/qTKEd8mcb1U.txt
- Transcript chars: 30210
- Keywords: security, actually, findings, server, request, little, components, threat, access, meetings, feature, together, interested, please, create, specific, published, recommendation

### Resumo baseado na transcript

well hello everyone what are some examples of two things that go together well I'll start peanut butter and jelly could I get a little audience participation here examples of two things that go together well cookies and milk salt and salt and chocolate one more what's one more example bacon and eggs excellent these are all excellent examples how about kubernetes in security my name is alla duberry I know you're all so surprised my [Applause] yes my name is Al duberry I have the pleasure of uh talking

### Excerpt da transcript

well hello everyone what are some examples of two things that go together well I'll start peanut butter and jelly could I get a little audience participation here examples of two things that go together well cookies and milk salt and salt and chocolate one more what's one more example bacon and eggs excellent these are all excellent examples how about kubernetes in security my name is alla duberry I know you're all so surprised my [Applause] yes my name is Al duberry I have the pleasure of uh talking about six security what we've been up to with my colleagues pushker savitha and Rey today so a little bit about what we do in Sig security as a whole so Sig security is a horizontal non-coding Sig that drives security initiatives for the entire kubernetes project so some examples are checking in with um other parts of the project the other sigs making sure that the core components of kubernetes are secure doing some vulnerability Management in addition to the four sub projects that you'll be hearing about today so what really makes us stand out as a sort of security organization is really our approach in that it is very open and community-driven uh I know I've definitely experienced that some of the organizations I've worked at the security organization being uh sort of a policy enforcer and um you know being a little bit regimented and with our open community-based approach what really comes across is that what gets done and what we focus on is really based on who comes to the meetings what are they excited about what interests them and what do they think is important about driving security forward in the project and that really speaks to our four Focus points which are four sub projects which are self assessments which is the sub project that I lead docs which is Seva tools which is pushker and uh let's see third party audit which we'll be talking about today which is driven by Ray now if you want to come and join the good trouble that we make hop into our slack channel uh Sig security also you can join our Google Group which will add you to all of the meetings including the bi-weekly Sig security meeting and all of the sub project meetings as well so first a little bit about self assessments the sub project that I lead uh there should be a picture here o there we go so this is the lightweight threat modeling sub project in kubernetes so our output is uh lightweight threat models totally shocking I know but the outcome that we're really trying to drive throu
