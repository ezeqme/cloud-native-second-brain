---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Ciprian Hacman", "Jack Francis", "Microsoft", "Michael McCune", "Josephine Pfeiffer", "Red Hat", "Justin Santa Barbara", "Google"]
sched_url: https://kccnceu2026.sched.com/event/2EoKz/from-static-tokens-to-attestation-the-evolution-of-secure-node-joining-ciprian-hacman-jack-francis-microsoft-michael-mccune-josephine-pfeiffer-red-hat-justin-santa-barbara-google
youtube_search_url: https://www.youtube.com/results?search_query=From+Static+Tokens+to+Attestation%3A+The+Evolution+of+Secure+Node+Joining+CNCF+KubeCon+2026
slides: []
status: parsed
---

# From Static Tokens to Attestation: The Evolution of Secure Node Joining - Ciprian Hacman & Jack Francis, Microsoft; Michael McCune & Josephine Pfeiffer, Red Hat; Justin Santa Barbara, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ciprian Hacman, Jack Francis, Microsoft, Michael McCune, Josephine Pfeiffer, Red Hat, Justin Santa Barbara, Google
- Schedule: https://kccnceu2026.sched.com/event/2EoKz/from-static-tokens-to-attestation-the-evolution-of-secure-node-joining-ciprian-hacman-jack-francis-microsoft-michael-mccune-josephine-pfeiffer-red-hat-justin-santa-barbara-google
- Busca YouTube: https://www.youtube.com/results?search_query=From+Static+Tokens+to+Attestation%3A+The+Evolution+of+Secure+Node+Joining+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre From Static Tokens to Attestation: The Evolution of Secure Node Joining.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EoKz/from-static-tokens-to-attestation-the-evolution-of-secure-node-joining-ciprian-hacman-jack-francis-microsoft-michael-mccune-josephine-pfeiffer-red-hat-justin-santa-barbara-google
- YouTube search: https://www.youtube.com/results?search_query=From+Static+Tokens+to+Attestation%3A+The+Evolution+of+Secure+Node+Joining+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=MIO3tDk0GnI
- YouTube title: From Static Tokens to Attestation: The Evoluti... Ciprian H, Jack Francis M, Josephine P, & Justin B
- Match score: 0.776
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/from-static-tokens-to-attestation-the-evolution-of-secure-node-joining/MIO3tDk0GnI.txt
- Transcript chars: 27223
- Keywords: secure, cluster, talking, control, whatever, machine, clouds, metadata, hardware, attestation, instance, little, minimum, question, joining, software, working, discussion

### Resumo baseado na transcript

So we will discuss about secure node joining obviously in the context of Kubernetes. Um and uh we hope to give you some insights onto that and hopefully have some plans for the future. So u but we've been having this uh debate at least us as maintainers for some time because we also have projects like Gaops cluster API and CVS and other people complaining about security. harm in the interest of trying to achieve security you know under some urgent circumstances. So setting things up not only to be able to join securely but also to make them you know robust for day two is is a huge huge challenge. And we don't have a unified way of talking about where does the attestation, where does the secure boot happen within a Kubernetes cluster.

### Excerpt da transcript

So we will discuss about secure node joining obviously in the context of Kubernetes. Um and uh we hope to give you some insights onto that and hopefully have some plans for the future. Uh with that in mind uh let's start with the present introductions. Uh my name is uh Cyprian. Uh I'm a software engineer at Microsoft working on platform engineering. I'm also an open-source contributor and maintainer for about the last eight years. Uh and I'm happy to continue with that for some time more. Thank you. Uh hi, I'm Justin Santa Barbara. I am a software engineer at Google. I've been working on the Kubernetes project for about uh 10ish years and have failed to solve this problem which makes me one of the least qualified people in this room to be talking on this topic. So I hope there are many questions that you will grill us on. >> I'm Jack Francis. I'm also a software engineer at Microsoft. Been working on Kubernetes basically as long as these folks. Also similarly guilty of not solving this problem before but looking forward to this discussion amongst all of us.

>> Yeah, I'm Josie. I work for Red Hat and uh um I uh maintain the uh Carpenter implementation for u IBM cloud and touch on different sik autoscaling projects every now and then. >> And uh I'm Michael McHugh. I'm also a software engineer at Red Hat. Uh I've been working on Kubernetes kind of in similar space and previously on OpenStack doing more stuff and I don't think we solved this on OpenStack either. So, I kind of feel like Justin here. >> Yeah. So, I I think we all agree that uh it's something that hasn't been solved. We've been trying to figure out who was supposed to solve it. Um sadly, no one said yes. So u but we've been having this uh debate at least us as maintainers for some time because we also have projects like Gaops cluster API and CVS and other people complaining about security. Uh, and we want to make this a good experience for everybody and secure, right? We want clusters to be secure, but we've seen our fair share of uh CVS and uh issues reported. Um so what are memorable things from your point of view as maintainers uh with regards to issues about insecure node joining >> oh sorry but sorry >> sure >> I'm not sure I want to go first here this is like confessing all of our sins um I I think there have been many there So they're all basically the same vulnerability.

The we put too much uh information into the metadata service, the instance metadata service, and that information is
