---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Community Governance"]
speakers: ["Tihomir Surdilovic", "Red Hat", "Doug Davis", "IBM"]
sched_url: https://kccnceu2021.sched.com/event/iE7G/cncf-serverless-wg-serverless-workflow-project-deep-dive-tihomir-surdilovic-red-hat-doug-davis-ibm
youtube_search_url: https://www.youtube.com/results?search_query=CNCF+Serverless+WG+-+Serverless+Workflow+Project+Deep+Dive+CNCF+KubeCon+2021
slides: []
status: parsed
---

# CNCF Serverless WG - Serverless Workflow Project Deep Dive - Tihomir Surdilovic, Red Hat & Doug Davis, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Tihomir Surdilovic, Red Hat, Doug Davis, IBM
- Schedule: https://kccnceu2021.sched.com/event/iE7G/cncf-serverless-wg-serverless-workflow-project-deep-dive-tihomir-surdilovic-red-hat-doug-davis-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=CNCF+Serverless+WG+-+Serverless+Workflow+Project+Deep+Dive+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre CNCF Serverless WG - Serverless Workflow Project Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE7G/cncf-serverless-wg-serverless-workflow-project-deep-dive-tihomir-surdilovic-red-hat-doug-davis-ibm
- YouTube search: https://www.youtube.com/results?search_query=CNCF+Serverless+WG+-+Serverless+Workflow+Project+Deep+Dive+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dsuo1VQQZ2E
- YouTube title: CNCF Serverless WG - Serverless Workflow Project Deep Dive - Tihomir Surdilovic & Doug Davis
- Match score: 0.869
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/cncf-serverless-wg-serverless-workflow-project-deep-dive/dsuo1VQQZ2E.txt
- Transcript chars: 26198
- Keywords: workflow, serverless, actually, events, define, language, little, function, definition, itself, particular, schema, definitions, currently, invoke, workflows, functions, runtime

### Resumo baseado na transcript

all right hi everybody and welcome to the serverless working group update uh tmr and i are going to be talking about two different projects today cloud events as well as the workflow specification so seymour can you go ahead and share your screens i think we're going to vanish now all right let's go and start the presentation and here we go so i'm going to be up first so let's go to the next slide obviously as i mentioned we're going to talk about cloud events give you

### Excerpt da transcript

all right hi everybody and welcome to the serverless working group update uh tmr and i are going to be talking about two different projects today cloud events as well as the workflow specification so seymour can you go ahead and share your screens i think we're going to vanish now all right let's go and start the presentation and here we go so i'm going to be up first so let's go to the next slide obviously as i mentioned we're going to talk about cloud events give you a quick update and then the bulk of the talk will be team we're talking about the serverless workflow spec all right so first obviously cloudevents so just a quick recap we delivered the latest version of the spec which is version 101 back in december of last year same deliverables as before and i'm not going to go into what the spec is i'm assuming everybody understands what that is or you can go find it this isn't that kind of call we're going to go into deep dive but just so you understand what the deliverables were it was obviously the specification itself the transport bindings the encoding formats a primer to give you guidance on why we did what we did how to use the spec stuff like that and a whole bunch of sdks to help you get started with cloud events okay now in terms of what's coming up next for the cloud events deck itself to be honest not a whole lot we are doing some minor bug fixes that people find but for the most part we're finding the spec is pretty much okay and we're just waiting for more community feedback to see if there are things we need to work on in the future but we're not just toiling our our fingers we're actually looking at the next set of pain points and as you can see here we're going to start looking at what we call sort of the life cycle of event delivery and from from beginning to end okay now crown events helps you deliver the event from the producer to the to the consumer itself but in order for that to actually get started what has to happen is the consumer first has to discover what event producers are out there and what the events are that they actually do produce okay so what we're going to be doing is working on a discovery api spec and that's going to allow producers to advertise that they're out there and what the events are that that people can't subscribe to so a consumer will then hit a discovery endpoint find out what their what events are out there who produces them how they can be delivered you know different transport protocols what are diff
