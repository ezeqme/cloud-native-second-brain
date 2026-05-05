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
themes: ["AI ML", "Security", "Kubernetes Core", "Community Governance"]
speakers: ["Anish Ramasekar", "Mo Khan", "Stanislav Láznička", "Rita Zhang", "Peter Engelbert", "Microsoft"]
sched_url: https://kccncna2025.sched.com/event/27Nld/strengthening-kubernetes-trust-sig-auths-latest-security-enhancements-anish-ramasekar-mo-khan-stanislav-laznicka-rita-zhang-peter-engelbert-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Strengthening+Kubernetes+Trust%3A+SIG+Auth%27s+Latest+Security+Enhancements+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Strengthening Kubernetes Trust: SIG Auth's Latest Security Enhancements - Anish Ramasekar, Mo Khan, Stanislav Láznička, Rita Zhang & Peter Engelbert, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Anish Ramasekar, Mo Khan, Stanislav Láznička, Rita Zhang, Peter Engelbert, Microsoft
- Schedule: https://kccncna2025.sched.com/event/27Nld/strengthening-kubernetes-trust-sig-auths-latest-security-enhancements-anish-ramasekar-mo-khan-stanislav-laznicka-rita-zhang-peter-engelbert-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Strengthening+Kubernetes+Trust%3A+SIG+Auth%27s+Latest+Security+Enhancements+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Strengthening Kubernetes Trust: SIG Auth's Latest Security Enhancements.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Nld/strengthening-kubernetes-trust-sig-auths-latest-security-enhancements-anish-ramasekar-mo-khan-stanislav-laznicka-rita-zhang-peter-engelbert-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Strengthening+Kubernetes+Trust%3A+SIG+Auth%27s+Latest+Security+Enhancements+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=SqdD9waaeno
- YouTube title: Strengthening Kubernetes Trust: SIG Auth's Latest Se... Anish R, Mo K, Stanislav L, Rita Z & Peter E
- Match score: 0.772
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/strengthening-kubernetes-trust-sig-auths-latest-security-enhancements/SqdD9waaeno.txt
- Transcript chars: 28432
- Keywords: feature, certificate, actually, cluster, tokens, volume, account, access, cublet, basically, specify, config, configure, credential, credentials, private, policy, probably

### Resumo baseado na transcript

The rest of the leads are either in the audience or it'll be shortly on stage. Uh I'll introduce David, Jordan, and Micah since they're not presenting today, but leave the rest to introduce themselves when they get here. But often as we all know there are ammon tasks like metrics and troubleshooting where those type of ammon workloads will require access to um these specialized devices that are already in use by other workloads. So this is what we thought okay why why don't we add this to um uh kubernetes core and with this feature uh the admin will basically be able to uh add a annotation to their namespace to ensure that only that nameace can uh So this started alpha and 129 and as the name suggests it's bringing some structure into how you configure authenticators in Kubernetes and prior to this you could configure an OIDC authenticator using flags which means you only could do one authenticator and if you But with this you can now configure multiple jot authenticators and jot authenticator is an authenticator that authenticates kubernetes users based on um jots.

### Excerpt da transcript

Thank you all for coming. Uh this is our uh SIGOT deep dive for this year. So we got a lot of stuff to talk about. So I'm going to try to keep it brisk here. Uh so I'm one of the tech leads for SIGO. The rest of the leads are either in the audience or it'll be shortly on stage. Uh I'll introduce David, Jordan, and Micah since they're not presenting today, but leave the rest to introduce themselves when they get here. Uh, and to help us present some of these, we have some good community members who I'll also ask to introduce themselves when they come on stage. Uh, but yeah, when I said a lot of stuff, we have a lot of stuff to talk about. Um, so we'll go into detail, but not too far. So this year we're going to do it a little different. We'll talk about the stuff that's coming up in 135 first because the list is shorter. Um, so I'm sure everyone has at least at some point used Kubernetes impersonation. Um so this release we implemented Jean and myself uh a new concept to it called constraint impersonation.

So traditionally impersonation has been sort of all or nothing right you can say you can impersonate Rita but you can't change anything after the fact right so if Rita is a cluster admin on that cluster then you're effectively cluster admin there's no scoping beyond that right so I like to use a really really tightly scoped example to explain it right which is um what if you want the service account running on a particular node to only be able to get pods while it's doing that right and when you intersect all the permissions through this, right? What that ends up meaning is that service account can now only read the pods for its node, right? Based on how it's getting scheduled, right? So, if you have a Damon set that's running across all your nodes, each individual instance of that service account, it's going to get a different view of the pods it can see, but all that's expressed in sort of one unified way. Uh, so I tried to stick the mermaid diagram to describe how all this works in here, and then I just gave up.

Uh, because this is like this is like a third of it. Um, the gist of it is the whole thing is still backwards compatible. All the old stuff still works exactly like it did before. Uh, but the new stuff was so dramatically different than the existing implementation that I effectively had to rewrite it from scratch. Uh, uh, so there's basically an if statement that says if the new thing is enabled, use the new handler, otherwise use the old han
