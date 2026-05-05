---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Mahamed Ali", "Cisco", "Benjamin Elder", "Google"]
sched_url: https://kccnceu2024.sched.com/event/1Yhix/kubernetes-infra-sig-intro-and-updates-mahamed-ali-cisco-benjamin-elder-google
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Infra+SIG%3A+Intro+and+Updates+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Kubernetes Infra SIG: Intro and Updates - Mahamed Ali, Cisco & Benjamin Elder, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Mahamed Ali, Cisco, Benjamin Elder, Google
- Schedule: https://kccnceu2024.sched.com/event/1Yhix/kubernetes-infra-sig-intro-and-updates-mahamed-ali-cisco-benjamin-elder-google
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Infra+SIG%3A+Intro+and+Updates+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Kubernetes Infra SIG: Intro and Updates.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhix/kubernetes-infra-sig-intro-and-updates-mahamed-ali-cisco-benjamin-elder-google
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Infra+SIG%3A+Intro+and+Updates+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1-OCYY-OG0A
- YouTube title: Kubernetes Infra SIG: Intro and Updates - Mahamed Ali, Cisco & Benjamin Elder, Google
- Match score: 0.735
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/kubernetes-infra-sig-intro-and-updates/1-OCYY-OG0A.txt
- Transcript chars: 15789
- Keywords: google, infrastructure, bucket, running, migrating, repository, projects, working, amount, testing, registry, access, finish, pipeline, release, cluster, inside, actually

### Resumo baseado na transcript

hello everyone thanks for coming at the end of cubec con it's been a long cubec con for me I'm sure it's been a long cubec con for you all uh bear withth me a little bit I'm losing my voice here but should be able to get through this uh welcome to the Sig K SIM for updates uh we'll be talking about what's been going on in the Kates infig and where we're going my name is Benjamin Elder I'm a software engineer at Google this Muhammad M so people can see what's going on with the infra we're going to do some cost optimization and we're going to migrate from GCR to AR the rest of the way um ahead of that deprecation I want to take a moment to thank all or the kubernetes testim for repo as you can see we run a lot um up at the top here that is a flame graph of the time to complete and the uh success or failure state of the jobs um over the past day have things tangled up in that we have been migrating them to run on kubernetes clusters run by the kubernetes project we are going to finish that by August all jobs must be migrated or they will be removed we've made a huge effort and Ricky has been doing a massive amount of effort to coordinate migrating CI jobs to the community infrastructure and we're getting really close so we also have this test triage pipeline basically we collect all the logs from our tests we get all the errors

### Excerpt da transcript

hello everyone thanks for coming at the end of cubec con it's been a long cubec con for me I'm sure it's been a long cubec con for you all uh bear withth me a little bit I'm losing my voice here but should be able to get through this uh welcome to the Sig K SIM for updates uh we'll be talking about what's been going on in the Kates infig and where we're going my name is Benjamin Elder I'm a software engineer at Google this Muhammad M uh SRE at Cisco and we are leads in the Sig so Mohammad is a Sig km for Tech lead and a native maintainer or is it can native now K native um and I'm on the kubernetes steering committee uh I'm a s Kate INF for and Sig testing Tech lead and I'm maintainer of kind so what is Sig Kat infra Sig Kate infra manages the kubernetes projects own infrastructure uh that includes the registry res serve the container images prow which is our CI system we'll talk more about that later d.c. that serves binaries and all of the expansive cicd infrastructure that we use um for running eede tests and all the things to make sure that the kubernetes project is reliable so what are our priorities this year we're migrating everything left that is running in some company's account to accounts in the Kuban project we've been working on this for a long time since the beginning of the Sig and we've hit one bump after another we're confident this year the last lingering things by the end of the year everything will be an account that is owned by the cncf and Sig Kate simra together with continuity through the project and where anybody can show up and participate we're going to adopt OCTA SSO to make it easier to onboard people into participating uh we've had some infrastructure that for gcp because that's the first vendor we had for managing access we're going to do multivendor access and make sure that contributors want to contribute we can get them quickly onboarded we're going to improve our observability stack so people can see what's going on with the infra we're going to do some cost optimization and we're going to migrate from GCR to AR the rest of the way um ahead of that deprecation I want to take a moment to thank all the vendors who've been sponsoring us uh Google cloud and Amazon who are providing $3 million a year each in Cloud credits fastly who's providing a huge amount of bandwidth for us uh equinex and digital ocean who are providing resources that we use for testing as well and more soon than you'll hear about later so I said we comple
