---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Security + Identity + Policy"
themes: ["Security"]
speakers: ["Ric Featherstone", "ControlPlane"]
sched_url: https://kccnceu2022.sched.com/event/ytsx/throw-away-your-passwords-trusting-workload-identity-ric-featherstone-controlplane
youtube_search_url: https://www.youtube.com/results?search_query=Throw+Away+Your+Passwords%3A+Trusting+Workload+Identity+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Throw Away Your Passwords: Trusting Workload Identity - Ric Featherstone, ControlPlane

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]]
- País/cidade: Spain / Valencia
- Speakers: Ric Featherstone, ControlPlane
- Schedule: https://kccnceu2022.sched.com/event/ytsx/throw-away-your-passwords-trusting-workload-identity-ric-featherstone-controlplane
- Busca YouTube: https://www.youtube.com/results?search_query=Throw+Away+Your+Passwords%3A+Trusting+Workload+Identity+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Throw Away Your Passwords: Trusting Workload Identity.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytsx/throw-away-your-passwords-trusting-workload-identity-ric-featherstone-controlplane
- YouTube search: https://www.youtube.com/results?search_query=Throw+Away+Your+Passwords%3A+Trusting+Workload+Identity+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=z-JxZblhCG8
- YouTube title: Throw Away Your Passwords: Trusting Workload Identity - Ric Featherstone, ControlPlane
- Match score: 0.856
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/throw-away-your-passwords-trusting-workload-identity/z-JxZblhCG8.txt
- Transcript chars: 26555
- Keywords: identity, account, cluster, workload, workloads, running, tokens, discovery, secrets, verify, credentials, spiffy, certificate, information, claims, access, documents, issuer

### Resumo baseado na transcript

all right good afternoon everybody welcome to throw away your passwords trusting workload identity my name's rick featherstone i'm a engineer at control plane for the last couple of years i've mostly been working with secrets management and machine identity i work for control plane we're a cloud native security consultancy we do security audits consultancy pen testing things like that hopefully you've had a chance to come to our stand and talk to people if you haven't pop over before you go home so on the left are the

### Excerpt da transcript

all right good afternoon everybody welcome to throw away your passwords trusting workload identity my name's rick featherstone i'm a engineer at control plane for the last couple of years i've mostly been working with secrets management and machine identity i work for control plane we're a cloud native security consultancy we do security audits consultancy pen testing things like that hopefully you've had a chance to come to our stand and talk to people if you haven't pop over before you go home so on the left are the things that i've claimed i'm going to talk about this afternoon and so we're talking about trust uh in the context of secrets management and access control but focusing primarily on machine identity what it is how do you get one we're up against the post lunchtime dip at the end of a long week so you're probably all as tired as as i am i'm going to attempt to cover a lot of ground in sort of 30 minutes or so i'm going to focus on concepts rather than going into too much depth on some of these things the idea is to give you options that you can kind of take away and apply to the things that you're doing when you get back to your day jobs just talking about some of the things that are available to you some of the things you might already know hopefully some of them you don't yet otherwise it's not going to be very interesting talk for you so historically infrastructure was reasonably static iop addresses were statically allocated so you could reasonably use these to represent your identity firewalls used ip and port combinations ip addresses were used in x509 certificates secrets and certificates were manually deployed to machines by admins you might use protocols like kerberos to initiate trust between machines if you didn't really like yourself very much but then cloud computing fundamentally changed the way that we do infrastructure ip addresses are no longer a useful identifier workloads come and go your workload will get a different ip address as it gets restarted you could have multiple instances of your workload so they've got multiple ip addresses at the same time secrets distribution becomes a much harder problem with these dynamic workloads how do you get the secrets on there with more services wanting to communicate with each other the old ip and boundary-based approaches that they no longer work sequence management solutions like hashicorp vault cloud secrets managers cloud kms they help with the sequence distribution but in order t
