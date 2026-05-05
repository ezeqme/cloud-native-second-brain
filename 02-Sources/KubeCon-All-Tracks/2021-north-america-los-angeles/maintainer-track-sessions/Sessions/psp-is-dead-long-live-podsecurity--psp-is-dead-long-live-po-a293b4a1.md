---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Monis Khan", "VMware", "Mike Danese", "Google"]
sched_url: https://kccncna2021.sched.com/event/lV9P/psp-is-dead-long-live-podsecurity-monis-khan-vmware-mike-danese-google
youtube_search_url: https://www.youtube.com/results?search_query=PSP+is+Dead%2C+Long+Live+PodSecurity+CNCF+KubeCon+2021
slides: []
status: parsed
---

# PSP is Dead, Long Live PodSecurity - Monis Khan, VMware; Mike Danese, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Monis Khan, VMware, Mike Danese, Google
- Schedule: https://kccncna2021.sched.com/event/lV9P/psp-is-dead-long-live-podsecurity-monis-khan-vmware-mike-danese-google
- Busca YouTube: https://www.youtube.com/results?search_query=PSP+is+Dead%2C+Long+Live+PodSecurity+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre PSP is Dead, Long Live PodSecurity.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV9P/psp-is-dead-long-live-podsecurity-monis-khan-vmware-mike-danese-google
- YouTube search: https://www.youtube.com/results?search_query=PSP+is+Dead%2C+Long+Live+PodSecurity+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yyr_cklZo3c
- YouTube title: PSP is Dead, Long Live PodSecurity - Monis Khan, VMware; Mike Danese, Google
- Match score: 0.721
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/psp-is-dead-long-live-podsecurity/yyr_cklZo3c.txt
- Transcript chars: 29235
- Keywords: security, checks, admission, controller, version, basically, deployment, policy, privileged, whatever, default, little, pretty, restricted, actually, trying, completely, change

### Resumo baseado na transcript

i'm mike and this is mo so um i will be doing uh this is technically the sig of deep dive so i'll be covering um a little bit of cigar stuff i'm gonna give you guys a highlight reel of what we've been working on over the past year or so because i know it's been a while since we talked and then i'll hand it off to mo who will begin the deep dive into pod security so let's get started so um sigoth what do we do entire ecosystem because those have significantly better security properties than legacy tokens there's some more work to do there and finally the last highlight is we have a sig sub project in uh called this secret csi driver they're actually implementations of um so csi is the canadian storage interface there are implementations of the secret csi driver with back-ends for aws azure gcp and vault and that allows configuring volumes that project secrets in external uh um secret storage providers so um i think the kep for gaining that we'll go over like what the evaluator and the checks are like but basically if you're if you're familiar with the kubernetes code base you're probably familiar with the builder pattern that we have and so all this is doing is like you know passing kind of the hope from this is that [Music] we want to enable people to build tooling off of this and you know offer value just outside of just pure kubernetes admission so the the notes um that i...

### Excerpt da transcript

i'm mike and this is mo so um i will be doing uh this is technically the sig of deep dive so i'll be covering um a little bit of cigar stuff i'm gonna give you guys a highlight reel of what we've been working on over the past year or so because i know it's been a while since we talked and then i'll hand it off to mo who will begin the deep dive into pod security so let's get started so um sigoth what do we do what are we responsible for um sig auth is primarily responsible for authentication authorizations the kubernetes api and various other security controls um such as uh admission and uh authorization policy like rbac and extensions therein so um one of the admissions that we're gonna be talking about today is uh pod security admission so what have we been doing for the past year or so there's actually been a lot going on so maybe actually probably over a year ago we began discussing the defecation of uh pod security policy um and uh discussing what it would mean to be a successor of pod security policy and we knew that pod security policy had a lot of users in open source like we debated whether we could defer those users to look at out of tree um strategies for for doing the same thing like opa ultimately we kind of landed on pod security which we will discuss in great depth that is going to be beta in the upcoming release of kubernetes we're targeting beta 123 targeting beta and 123.

um the certificates api which had uh was long overdue for ga finally launched ga in 119. um i think it had been around in beta since like 1-6 so it's like maybe three years overdue for going ga um before the ga some some notable changes were uh added such as a new signer name api so now the api can be divided between uh multiple consumers um after ga a duration hint was added so now you can sign certificates or you can request uh certificates for specific durations um the exec auth cube control plugin and extension uh also went ga in 122 i think um which uh it was either 121 or 122. i can't actually remember it no i think it's 120 um and that paves the way for moving some of the final entry uh authentication plugins for clouds out of tree so that's kind of part of the whole club provider extraction effort and we also have a proposal to extend support for those plugins to um to request signing and like mutual tls protocols and the token request api bound service account token volume and um uh provisioning uh for bound service cat tokens to replace like the legacy secret
