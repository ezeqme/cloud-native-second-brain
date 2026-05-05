---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["Security"]
speakers: ["Ashley Davis", "Jetstack"]
sched_url: https://kccnceu2023.sched.com/event/1HyZ6/rotate-roots-right-round-using-cert-manager-for-safer-private-pki-ashley-davis-jetstack
youtube_search_url: https://www.youtube.com/results?search_query=Rotate+Roots+Right+Round%3A+Using+Cert-Manager+for+Safer+Private+PKI+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Rotate Roots Right Round: Using Cert-Manager for Safer Private PKI - Ashley Davis, Jetstack

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[Security]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ashley Davis, Jetstack
- Schedule: https://kccnceu2023.sched.com/event/1HyZ6/rotate-roots-right-round-using-cert-manager-for-safer-private-pki-ashley-davis-jetstack
- Busca YouTube: https://www.youtube.com/results?search_query=Rotate+Roots+Right+Round%3A+Using+Cert-Manager+for+Safer+Private+PKI+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Rotate Roots Right Round: Using Cert-Manager for Safer Private PKI.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyZ6/rotate-roots-right-round-using-cert-manager-for-safer-private-pki-ashley-davis-jetstack
- YouTube search: https://www.youtube.com/results?search_query=Rotate+Roots+Right+Round%3A+Using+Cert-Manager+for+Safer+Private+PKI+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=uvL7SHhVKUY
- YouTube title: Rotate Roots Right Round: Using Cert-Manager for Safer Private PKI - Ashley Davis, Jetstack
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/rotate-roots-right-round-using-cert-manager-for-safer-private-pki/uvL7SHhVKUY.txt
- Transcript chars: 26150
- Keywords: certificate, manager, certificates, private, cluster, policy, actually, rotation, issuer, config, encrypt, bundle, create, intermediate, simple, self-signed, running, update

### Resumo baseado na transcript

hey welcome to rotate Roots right round using cert manager for safer private pki you don't need to know what cert manager is and you don't need to know what pki is hopefully by the end of this you'll know and want to use both of them but obviously it will help if you do know both of those tools I'm Ash here's a picture of me with a lot less hair I'm a senior software engineer at jet stack by venify I've provided a loads of load of ways

### Excerpt da transcript

hey welcome to rotate Roots right round using cert manager for safer private pki you don't need to know what cert manager is and you don't need to know what pki is hopefully by the end of this you'll know and want to use both of them but obviously it will help if you do know both of those tools I'm Ash here's a picture of me with a lot less hair I'm a senior software engineer at jet stack by venify I've provided a loads of load of ways you could reach me here feel free to reach out I'm happy to talk always interested in talking about certificates to the point where actually I did a live stream recently where I was described as a professional certificate nerd and I'm kind of going to wear that as pride and take that as my new title going forward I'm also a manager maintainer which is helpful because I'll be talking about cert manager a lot in this talk without further Ado let's jump into it what is cert manager we need to make sure that everyone's on the same page before we start cert manager is the easiest way to automatically manage certificates in kubernetes clusters we like to say this because it's kind of a guiding mantra for us we're trying to aim for this in everything that we do you can actually see this quote at the beginning of every cert manager release that we create that's because well technically it's because when we share the release on social media this is the line that we want people to see there's just a little Insider detail but this really does matter to us and it's what we try to do certain manager is a cncf incubating project that's part of why I'm here today at kubecon but it's also kind of unique in its role by that I mean cert manager is really the only tool in the cncf as far as I can see which kind of does what it does and that is it helps you to manage certificates on kubernetes we've also regionally recently reached the Milestone of hitting 10 000 stars on GitHub which is a really different kind of achievement to being cncf incubating but still a really satisfying and cool one and we're really chuffed about that the core of cert manager is really the issuer by issuer I mean how does cert manager know where to get certificates from and that's a decision that you get to make in this talk we'll be talking about the ca issuer which is built into cert manager but actually there are loads here I've given an example of hashicot vault genify which is my employer and let's encrypt let's encrypt or Acme is probably the most popular choice
