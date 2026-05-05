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
themes: ["AI ML", "Community Governance"]
speakers: ["Ashley Davis", "Maël Valais", "Tim Ramlot", "Venafi"]
sched_url: https://kccnceu2024.sched.com/event/1Yhiu/cryptographically-signed-swag-cert-managers-stamped-certificates-ashley-davis-mael-valais-tim-ramlot-venafi
youtube_search_url: https://www.youtube.com/results?search_query=Cryptographically+Signed+Swag%3A+Cert-Manager%E2%80%99s+Stamped+Certificates+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Cryptographically Signed Swag: Cert-Manager’s Stamped Certificates - Ashley Davis, Maël Valais & Tim Ramlot, Venafi

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Ashley Davis, Maël Valais, Tim Ramlot, Venafi
- Schedule: https://kccnceu2024.sched.com/event/1Yhiu/cryptographically-signed-swag-cert-managers-stamped-certificates-ashley-davis-mael-valais-tim-ramlot-venafi
- Busca YouTube: https://www.youtube.com/results?search_query=Cryptographically+Signed+Swag%3A+Cert-Manager%E2%80%99s+Stamped+Certificates+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Cryptographically Signed Swag: Cert-Manager’s Stamped Certificates.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhiu/cryptographically-signed-swag-cert-managers-stamped-certificates-ashley-davis-mael-valais-tim-ramlot-venafi
- YouTube search: https://www.youtube.com/results?search_query=Cryptographically+Signed+Swag%3A+Cert-Manager%E2%80%99s+Stamped+Certificates+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vEeyZcQuD_A
- YouTube title: Cryptographically Signed Swag: Cert-Manager’s Stamped Certificates
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/cryptographically-signed-swag-cert-managers-stamped-certificates/vEeyZcQuD_A.txt
- Transcript chars: 30137
- Keywords: manager, certificate, actually, certificates, resource, basically, clusters, private, course, secret, question, obviously, created, cluster, printed, subject, request, solution

### Resumo baseado na transcript

okay I make that 5 minutes to so let's get started um quick admin beforehand we've heard a few alarms going off it's because the French government are testing the alarm system apparently you can't really prepare for that with a talk so like uh we'll see how that goes if your phone goes off it's okay please just get it if if you can it's no problem so uh let's get into the actual talk welcome to cryptographically signed swag thank you all for coming here bonjour uh I

### Excerpt da transcript

okay I make that 5 minutes to so let's get started um quick admin beforehand we've heard a few alarms going off it's because the French government are testing the alarm system apparently you can't really prepare for that with a talk so like uh we'll see how that goes if your phone goes off it's okay please just get it if if you can it's no problem so uh let's get into the actual talk welcome to cryptographically signed swag thank you all for coming here bonjour uh I hope you've had a good cubec con uh the scheduling means that obviously you've come here after the project Pavilion is closed so we're talking about the booth which you cannot go to that's a shame but what we can do is tell you what happened at the booth and maybe at Salt Lake City in November we'll be able to see you there and you can get a certificate there um so we are three C manager maintainers my name's Ash this is Tim and this is myel uh we all happen to work at venite and uh we spend at least part of our time maintaining C manager uh quick show of who has heard of C manager yeah that's what we like to see uh who runs C manager who runs C manager in production yeah great see you're all experts already you don't need to listen um just in case anyone doesn't know um C manager is what we like to say is the best way to get certificates in kubernetes so uh you're used to writing yaml to get a pod SE manager adds the ability to write yaml to get a certificate uh that you can use for for your website say or for interpod communication with encryption um the key really is that once you've told certain manager how to get a certificate you can actually like it already knows so it can renew the certificate as well and it won't expire and cause an outage and that's always good of course we support um various different ways of getting your uh certificate that includes Acme let encrypt that's what most people use but we can also do private pki which is kind of what we'll be talking about today in a way hashy cop Vault and a bunch other including Veni um there's a picture here and you might recognize uh some of the faces on it uh certainly my shiny head um this is what the booth looked like and this is what we'll be talking about today and this is the result of that so this is a stamped SE manager certificate that was issued by SE manager and then printed out in physical form I can't show you the other side because it has a QR code on it which would let you download my certificate so I'm I'm being reall
