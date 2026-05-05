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
themes: ["AI ML", "Community Governance"]
speakers: ["Kapil Thangavelu", "Stacklet"]
sched_url: https://kccncna2023.sched.com/event/1R2pO/cloud-custodian-state-of-the-mop-kapil-thangavelu-stacklet
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Custodian+-+State+of+the+Mop+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Cloud Custodian - State of the Mop - Kapil Thangavelu, Stacklet

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Kapil Thangavelu, Stacklet
- Schedule: https://kccncna2023.sched.com/event/1R2pO/cloud-custodian-state-of-the-mop-kapil-thangavelu-stacklet
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Custodian+-+State+of+the+Mop+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Cloud Custodian - State of the Mop.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2pO/cloud-custodian-state-of-the-mop-kapil-thangavelu-stacklet
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Custodian+-+State+of+the+Mop+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YRJqgY6vizM
- YouTube title: Cloud Custodian - State of the Mop - Kapil Thangavelu, Stacklet
- Match score: 0.791
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/cloud-custodian-state-of-the-mop/YRJqgY6vizM.txt
- Transcript chars: 15872
- Keywords: resources, providers, policy, custodian, actually, support, security, resource, little, policies, capabilities, looking, write, provider, capability, across, arbitrary, getting

### Resumo baseado na transcript

uh this is a maintainer track talk about Cloud custodian and where things are today so to do a little bit of intro for people that may or may not be familiar with Cloud custodian uh it's an open source project Apache 2.0 it's a cntf incubating project U and what it is it's a rules engine for helping you manage your Cloud accounts uh as well as being able to enforce those policies uh on your IAT code before deployment um so both runtime shift right and left um

### Excerpt da transcript

uh this is a maintainer track talk about Cloud custodian and where things are today so to do a little bit of intro for people that may or may not be familiar with Cloud custodian uh it's an open source project Apache 2.0 it's a cntf incubating project U and what it is it's a rules engine for helping you manage your Cloud accounts uh as well as being able to enforce those policies uh on your IAT code before deployment um so both runtime shift right and left um it's a simple yaml DSL uh very declarative very easy to read where you write you query a particular resource you do some arbitrary set of filtering on that and then you take a set of actions it's sort of Best in Class at doing actually fixing problems in terms of doing remediation it supports doing real-time enforcement by integrating with the cloud providers seress and event run times um so that as API calls are happening you can interspect them and make sure that they're compliant to policy uh it's stateless tool and uh we support multiple providers uh most of the big public clouds as well as kubernetes open sack and teror Forum which we will go into in a minute um it's used in production by thousands of companies um uh we we even occasionally get uh reach outs from the cloud providers before they do an incompatible update so that we don't they don't break their own users um and we've got about uh about 1,200 people in the in the custodian slack and about 3,000 in the finops clock custodian room as well uh just to see what uh some use cases are that people use this stuff for uh going to cover off on a couple categories uh one that's been popular the last a little while is something around is the fops use cases so find the old things take out the garbage on snapshots on setting up life cycles on S3 buckets on turning things off when not use on finding the underutilized uh things and and getting rid of them so uh super helpful for sort of cutting down on waste um and uh being more efficient about your Cloud spend uh Security's always been one of the cudan core use cases uh and it allows you to uh make do all kinds of things from setting making sure everything's encrypted um with custom manage Keys uh making sure that things are accessible from the network that Resources with embedded policies um are only accessible to the Right audience um and then of course being able to do incident response and it ties into the the cloud providers native tools so uh this is all about being you know taking being the
