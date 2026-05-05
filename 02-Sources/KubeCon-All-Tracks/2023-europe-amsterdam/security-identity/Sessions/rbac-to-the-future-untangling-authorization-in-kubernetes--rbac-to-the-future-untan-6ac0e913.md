---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["Security", "Kubernetes Core"]
speakers: ["Jimmy Mesta", "KSOC"]
sched_url: https://kccnceu2023.sched.com/event/1HyQC/rbac-to-the-future-untangling-authorization-in-kubernetes-jimmy-mesta-ksoc
youtube_search_url: https://www.youtube.com/results?search_query=%F0%9F%A6%9D+RBAC+to+the+Future%3A+Untangling+Authorization+in+Kubernetes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# 🦝 RBAC to the Future: Untangling Authorization in Kubernetes - Jimmy Mesta, KSOC

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jimmy Mesta, KSOC
- Schedule: https://kccnceu2023.sched.com/event/1HyQC/rbac-to-the-future-untangling-authorization-in-kubernetes-jimmy-mesta-ksoc
- Busca YouTube: https://www.youtube.com/results?search_query=%F0%9F%A6%9D+RBAC+to+the+Future%3A+Untangling+Authorization+in+Kubernetes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre 🦝 RBAC to the Future: Untangling Authorization in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyQC/rbac-to-the-future-untangling-authorization-in-kubernetes-jimmy-mesta-ksoc
- YouTube search: https://www.youtube.com/results?search_query=%F0%9F%A6%9D+RBAC+to+the+Future%3A+Untangling+Authorization+in+Kubernetes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3bE7o0-1CHY
- YouTube title: 🦝 RBAC to the Future: Untangling Authorization in Kubernetes - Jimmy Mesta, KSOC
- Match score: 0.95
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/rbac-to-the-future-untangling-authorization-in-kubernetes/3bE7o0-1CHY.txt
- Transcript chars: 24074
- Keywords: cluster, access, pretty, server, namespace, secrets, security, actually, probably, account, authorization, bindings, little, identity, called, default, interesting, important

### Resumo baseado na transcript

ready to talk about our back everybody's favorite subject right yes we love our back um I have candy imported straight from Los Angeles uh for the best questions or whoever wants it when we're done so I was told Laffy Taffy Atomic Fireballs yeah and that's it but yes please come see me after the talk uh so we're going to discuss are back uh and hopefully we can have fun while talking about our friend role-based access control so if you want the slides uh now later this

### Excerpt da transcript

ready to talk about our back everybody's favorite subject right yes we love our back um I have candy imported straight from Los Angeles uh for the best questions or whoever wants it when we're done so I was told Laffy Taffy Atomic Fireballs yeah and that's it but yes please come see me after the talk uh so we're going to discuss are back uh and hopefully we can have fun while talking about our friend role-based access control so if you want the slides uh now later this you can go to this tinyurl.com rbac Dash two dash the dash future um I promise it's not malware so we're gonna not really talk about what kubernetes is I assume we're good right everybody talks about that uh we'll have a one one slide one second and we'll talk about that and why identity is so freaking important these days right who you are what you can do what you have access to and why we're kind of uh missing out in kubernetes there's a lot of opportunity to do this better then terminology roles cluster roles role bindings verbs subjects all these things that we may deal with every day and they could be net new so we're going to just cover that and then a little bit of the authen auth C flow and most importantly some gotchas so uh I've given this talk one time before uh like three months ago in Norway and since then we have a new cve that was released last week that's super exciting along the lines of our back and privilege escalation which is uh well bad and good so let's dive in we know what kubernetes is it's really really important or we wouldn't be here we're running it everywhere people access kubernetes and robots do too right service accounts or or programmatic access and that's enough about that so identity is the new perimeter right we have lots and lots of vendors downstairs talking about just in time access and kind of auditing access to things and who you know zero trust we hear this this phrase thrown around a lot but what does that mean in kubernetes right and it's kind of a complicated relationship right just because you have a token or a certificate or you have an IAM role or something in your cloud provider that doesn't mean you should automatically be granted access to every single cluster and have cluster admin so it's a very um tangled web of configuration and that's kind of why we're working on untangling it um I haven't even watched Back to the Future in probably 10 years but I thought it sounded good so there will be references sprinkled throughout uh hopefully you
