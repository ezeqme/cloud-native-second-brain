---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Charlie Egan", "Styra", "Rita Zhang", "Microsoft"]
sched_url: https://kccncna2024.sched.com/event/1hoxC/open-policy-agent-opa-intro-deep-dive-v10-update-charlie-egan-styra-rita-zhang-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Open+Policy+Agent+%28OPA%29+Intro%2C+Deep+Dive+%26+V1.0+Update+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Open Policy Agent (OPA) Intro, Deep Dive & V1.0 Update - Charlie Egan, Styra & Rita Zhang, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Charlie Egan, Styra, Rita Zhang, Microsoft
- Schedule: https://kccncna2024.sched.com/event/1hoxC/open-policy-agent-opa-intro-deep-dive-v10-update-charlie-egan-styra-rita-zhang-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Open+Policy+Agent+%28OPA%29+Intro%2C+Deep+Dive+%26+V1.0+Update+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Open Policy Agent (OPA) Intro, Deep Dive & V1.0 Update.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoxC/open-policy-agent-opa-intro-deep-dive-v10-update-charlie-egan-styra-rita-zhang-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Open+Policy+Agent+%28OPA%29+Intro%2C+Deep+Dive+%26+V1.0+Update+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QuotLxFb2f4
- YouTube title: Open Policy Agent (OPA) Intro, Deep Dive & V1.0 Update - Charlie Egan, Styra & Rita Zhang, Microsoft
- Match score: 0.79
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/open-policy-agent-opa-intro-deep-dive-v1-0-update/QuotLxFb2f4.txt
- Transcript chars: 30274
- Keywords: policy, actually, gatekeeper, policies, write, enforcement, allows, engine, particular, request, decision, basically, metrics, support, working, interested, server, feature

### Resumo baseado na transcript

okay so um hello everybody my name is Charlie I work on the OPA team and the Deval team at styra uh and this is Rita hey everyone mic checked okay uh I'm Rita I am a opal gatekeeper maintainer I work at Microsoft and how it's going to work is I'm going to give a quick overview of opa and policy as code I'm going to go through um some updates around Opa 10 and then re is going to give a quick update about some changes recent changes

### Excerpt da transcript

okay so um hello everybody my name is Charlie I work on the OPA team and the Deval team at styra uh and this is Rita hey everyone mic checked okay uh I'm Rita I am a opal gatekeeper maintainer I work at Microsoft and how it's going to work is I'm going to give a quick overview of opa and policy as code I'm going to go through um some updates around Opa 10 and then re is going to give a quick update about some changes recent changes in the OPA gatekeeper project as well so I wanted to start out by asking or getting people to think about what is policy when I think about policy uh policy is a way of defining allowed operations and controls uh in system behaviors so common policies that those of us here today will be working with uh things like authorizing users based on organizational security requirements controlling which teams are deployed what into kubernetes uh implementing API access controls data filtering cicd permissions these are all things that uh I think of as policy uh anywhere that you're implementing Behavior which is uh boils down to something that looks like rules that's what policy is this is an example policy here so uh we have a policy here which is defining around uh permissions around deployments to production uh in an edge case where there's an perhaps an an incident and we have an En call a member of the en call support team and they have permissions that are different based on the time of day based on whether they're in the team and the environment that they're deploying to uh so this is a policy which is easily expressed in in English in natural language and um we're interested in codifying these policies so what's policiy is code so rather than talking about policies and uh you know it could be that that person who's on call needed to phone someone else and ask whether they could have extra permissions at the weekend to fix something in production or we could have codified that policy so that uh that that permission could have been granted in an automated way and so here's an example of what that policy might look like as code as you can see by default we deny the request to deploy to production but if it's the weekend and support is in the user's roles and the supports user is in the list of oncore users then this request would actually be allowed and when we write policers code like this uh it allows us to to automate these policy checks and the idea is that when you start thinking about your functionality all of the policy use c
