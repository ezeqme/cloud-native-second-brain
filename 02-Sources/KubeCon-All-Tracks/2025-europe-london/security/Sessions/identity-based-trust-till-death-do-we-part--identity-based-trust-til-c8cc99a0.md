---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Security"
themes: ["AI ML", "Security"]
speakers: ["John Kjell", "ControlPlane", "Kairo De Araujo", "Independent"]
sched_url: https://kccnceu2025.sched.com/event/1tx8L/identity-based-trust-till-death-do-we-part-john-kjell-controlplane-kairo-de-araujo-independent
youtube_search_url: https://www.youtube.com/results?search_query=Identity-based+Trust+-+Till+Death+Do+We+Part%3F+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Identity-based Trust - Till Death Do We Part? - John Kjell, ControlPlane & Kairo De Araujo, Independent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: United Kingdom / London
- Speakers: John Kjell, ControlPlane, Kairo De Araujo, Independent
- Schedule: https://kccnceu2025.sched.com/event/1tx8L/identity-based-trust-till-death-do-we-part-john-kjell-controlplane-kairo-de-araujo-independent
- Busca YouTube: https://www.youtube.com/results?search_query=Identity-based+Trust+-+Till+Death+Do+We+Part%3F+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Identity-based Trust - Till Death Do We Part?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx8L/identity-based-trust-till-death-do-we-part-john-kjell-controlplane-kairo-de-araujo-independent
- YouTube search: https://www.youtube.com/results?search_query=Identity-based+Trust+-+Till+Death+Do+We+Part%3F+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=26p_qvuCy-s
- YouTube title: Identity-based Trust - Till Death Do We Part? - John Kjell & Kairo De Araujo
- Match score: 0.837
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/identity-based-trust-till-death-do-we-part/26p_qvuCy-s.txt
- Transcript chars: 22061
- Keywords: metadata, policy, signature, process, everything, client, download, artifact, certificate, attestations, signatures, software, private, github, identity, actually, verify, pipeline

### Resumo baseado na transcript

Uh just started on Monday, so I know mostly about what the company does through the interview process. Uh I'm also a co-chair for the CNCF security tag and a maintainer on witness and archavista um which are sub projects underneath into um and I've contributed to uh things like the salsa project and other things. So um but what the problem and how you share uh new trusted keys uh if you lost your private key or this private key got leaked. but could be uh the docker hub or harbor or even your JROG in your organization and you have the tough metadata that's usually stored outside of uh this uh the same storage uh but you can have leave it together there's no uh problem the keys um it will download uh other metadata that I will not go in details here but basically it's the time stamp that will guarantee that your your uh artifact storage where is your or your registry it's a uh updated and also the And it was a way also to demonstrate that if you didn't wrote a good uh policy in your pipeline, it could anyway.

### Excerpt da transcript

I'm uh John Shell uh at Control Plane. Uh just started on Monday, so I know mostly about what the company does through the interview process. Um but we have a booth here too. Uh I'm also a co-chair for the CNCF security tag and a maintainer on witness and archavista um which are sub projects underneath into um and I've contributed to uh things like the salsa project and other things. Yeah, my name is Ka. I'm a open source software engineer as well. I'm a maintainer of tough python tough library and uh also uh archive vista an input project as well and we are here to talk about identity based trust. All right. So just to prepare you all um we're going to talk about the ento project the tough projects implementations underneath each of those and the sig store project and its different components. Um this is a lot uh I apologize in advance uh hopefully your brains don't melt um preparing this ours did slightly. So um the other thing that this does not include is uh introduction to uh the cryptography or X509 certificates or the underlying technologies that have made all of these different projects possible.

Um so we will be well I will be available for as long as needed afterwards uh for follow-on conversations. We also have um each of these projects in the project pavilion so feel free to stop by there as well too. um in toto and the update framework have both had people write entire PhDs on them. So we will try to do them just as we can in in the amount of time we have. Okay. Um let's start about signing and uh how we used to do in old days actually we still doing that. So how it works uh in general basically you have a private and public key uh that uh it's from some person or some organization and based on that you use your private key to sign some artifact and uh of course you keep your uh private key saved and it generates for you an um an signature uh and uh as your private key is saved you share share your public key basically and other people can just get the private key uh the public key and a signature and validate the um the artifact signature. So um but what the problem and how you share uh new trusted keys uh if you lost your private key or this private key got leaked.

So the solution is quite uh easy. You generate a new key, you resign the package with the new key and you publish your uh public key, new public key and you need to tell in a trust way to your users to use the new public key, right? And after resign everything you need to I'll t
