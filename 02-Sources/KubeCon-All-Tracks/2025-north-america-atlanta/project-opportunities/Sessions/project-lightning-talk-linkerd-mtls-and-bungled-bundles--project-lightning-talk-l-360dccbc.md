---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["Project Opportunities"]
speakers: ["Flynn", "Technical Evangelist"]
sched_url: https://kccncna2025.sched.com/event/28j3V/project-lightning-talk-linkerd-mtls-and-bungled-bundles-flynn-technical-evangelist
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Linkerd%2C+mTLS%2C+and+Bungled+Bundles+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Linkerd, mTLS, and Bungled Bundles - Flynn, Technical Evangelist

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Project Opportunities]]
- País/cidade: United States / Atlanta
- Speakers: Flynn, Technical Evangelist
- Schedule: https://kccncna2025.sched.com/event/28j3V/project-lightning-talk-linkerd-mtls-and-bungled-bundles-flynn-technical-evangelist
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Linkerd%2C+mTLS%2C+and+Bungled+Bundles+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Linkerd, mTLS, and Bungled Bundles.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/28j3V/project-lightning-talk-linkerd-mtls-and-bungled-bundles-flynn-technical-evangelist
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Linkerd%2C+mTLS%2C+and+Bungled+Bundles+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PpV8tAbBvsU
- YouTube title: Project Lightning Talk: Linkerd, mTLS, and Bungled Bundles - Flynn, Technical Evangelist
- Match score: 0.883
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-linkerd-mtls-and-bungled-bundles/PpV8tAbBvsU.txt
- Transcript chars: 5031
- Keywords: certificates, anchor, mesh, everything, actually, manager, certificate, bundle, linker, flames, rotation, linkerd, bundles, linkerty, bundled, familiar, security, application

### Resumo baseado na transcript

I'm here to talk to you from the linky project about linkerty mtls and the sad tale of bundled bundled bundles which is actually hard to even say. Our job is to add security reliability and observability to your entire application down at the platform level so that you do not have to change your application. The default was never prior to 1.18 in manager.8 18 they changed the defaults to always which is great for security uh because that means that when it rotates it it will actually give it a new key.

### Excerpt da transcript

So I'm Flynn. I'm here to talk to you from the linky project about linkerty mtls and the sad tale of bundled bundled bundles which is actually hard to even say. If you are not familiar with linkerty we are a service mesh. Our job is to add security reliability and observability to your entire application down at the platform level so that you do not have to change your application. The very first step of this is that we take over the network and we use ultra lightweight ultraast rust microproxies to go and inject MTLS into all of your meshed communications which permits us a lot of interesting functionality. If you're familiar with MTLS, you will know that the basis of identity in MTLS is certificates. And in fact, our sad tale begins with a linker to user calling up to say that their certificates had expired and everything had gone up in flames. So, if you have gotten this far in cloud native without knowing anything else about certificates, first off, congratulations. I'm impressed. But also, there are a couple of things that you need to know about certificates to understand the rest of our sad tale of two different issues combining to cause misery.

The first one is that for linkertd to use a certificate, it has to be ultimately derived from a cert called a trust anchor which lives in a trust bundle. The second thing that you need to know here is that for example, if you've got this blue anchor, you have blue certificates. Everything is well. This is good because linkertd knows that it can trust those blue certificates in the mesh. To prevent these things from expiring though, you have to rotate them or renew them. And if you need to do that to a trust anchor, you have to do something special. You start by generating a shiny new red trust anchor. Then you start rotating certificates down in the mesh. This transition state in the middle right now, this is fine. We've got rederts and blueerts in the mesh. We've got a red anchor and a blue anchor in the bundle. Everything is happy. Eventually, you have only rederts in the mesh. And then you can kick the blue bundle out. All is good. That brings us to our first of two problems. Uh, turns out there were some old linkery docs that described a wrong way to do this rotation.

They said to do the rotation this way. That does not work because now you have blueerts down in the mesh, but you only have a redert in the bundle and everything again goes up in flames. Now, a fair question would be, hey, did you guys not
