---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Security + Identity + Policy"
themes: ["Security", "Kubernetes Core"]
speakers: ["Ian Coldwater", "Twilio", "Brad Geesaman", "Aqua Security"]
sched_url: https://kccncna2021.sched.com/event/lV0h/kubernetes-exposed-seven-of-nine-hidden-secrets-that-will-give-you-pause-ian-coldwater-twilio-brad-geesaman-aqua-security
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Exposed%21+Seven+of+Nine+Hidden+Secrets+That+Will+Give+You+Pause+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Kubernetes Exposed! Seven of Nine Hidden Secrets That Will Give You Pause - Ian Coldwater, Twilio & Brad Geesaman, Aqua Security

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Ian Coldwater, Twilio, Brad Geesaman, Aqua Security
- Schedule: https://kccncna2021.sched.com/event/lV0h/kubernetes-exposed-seven-of-nine-hidden-secrets-that-will-give-you-pause-ian-coldwater-twilio-brad-geesaman-aqua-security
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Exposed%21+Seven+of+Nine+Hidden+Secrets+That+Will+Give+You+Pause+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Kubernetes Exposed! Seven of Nine Hidden Secrets That Will Give You Pause.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV0h/kubernetes-exposed-seven-of-nine-hidden-secrets-that-will-give-you-pause-ian-coldwater-twilio-brad-geesaman-aqua-security
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Exposed%21+Seven+of+Nine+Hidden+Secrets+That+Will+Give+You+Pause+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JBbVTmrZ45E
- YouTube title: Kubernetes Exposed! Seven of Nine Hidden Secrets That Will Give You... Ian Coldwater & Brad Geesaman
- Match score: 0.911
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/kubernetes-exposed-seven-of-nine-hidden-secrets-that-will-give-you-pau/JBbVTmrZ45E.txt
- Transcript chars: 24724
- Keywords: cluster, default, control, validating, traffic, external, server, actually, create, session, security, second, important, always, policy, privileged, another, masters

### Resumo baseado na transcript

uh my name is kat cosgrove i am your moderator for this session and this is kubernetes exposed seven of nine hidden secrets that will give you pause presented by the incomparable ian coldwater of twilio and brad giesemann of aqua security just a reminder please hold your questions until after the session is over then you can raise your hand and i will come find you with a microphone or you can ask in the meeting play app enjoy the talk [Applause] hi everybody can you hear me y'all role binding it's gone right like that seems like that would be sensible but it doesn't always work that way there's one special exception and it can be a dangerous one that exception is system masters which is hard coded in kubernetes to be cluster to port 9443 gets redirected to port 80 on nginx so what's going to happen nginx is going to go i don't know what to do with this and just send back an error right the actual attack is kind of interesting we scale the deployment of engine x up to two so we add another engine x pod then we try to submit the privilege pod then we scale engine up engine x up to three and then we immediately scale it back down to two now why would

### Excerpt da transcript

uh my name is kat cosgrove i am your moderator for this session and this is kubernetes exposed seven of nine hidden secrets that will give you pause presented by the incomparable ian coldwater of twilio and brad giesemann of aqua security just a reminder please hold your questions until after the session is over then you can raise your hand and i will come find you with a microphone or you can ask in the meeting play app enjoy the talk [Applause] hi everybody can you hear me y'all in the back too sounds good fabulous okay hi welcome to kubernetes exposed seven of nine hidden secrets that will give you pause if you are in the room for another talk you are in the wrong room and that's okay we can hang out anyway my name is ian coldwater i am co-chair of kubernetes security and i have container things hi i'm brad i'm director of cloud security at aqua security and i also hack container things if you're new to kubernetes you may have noticed some things along your way that make you go hmm some unexpected behaviors maybe some weird surprises if this sounds familiar to you you're not alone we've been working with kubernetes for a while now and we've seen a lot of strange behaviors wild surprises unexpected gadgets things that don't always work the way they think the way you think they will and frankly there are a lot of things that you might not be aware of that you might not need to know so today we figured we'd share some of those with you grab your popcorn and your 3d glasses and let's explore some of the hidden secrets weird science and fun twists and turns in the land of kubernetes watch out for jump scares so here's a quick one you might think that since kubernetes heavily uses pki for authentication that there would be a way to revoke a specific certificate if one of the certificate pairs ever got compromised that would be sensible right that seems like that would make sense but that's not actually how that works ofc sp stapling is not supported this is a long time issue in kubernetes like no literally a long time issue there is a kubernetes issue from 2015 about this specifically so wait really what do you have to do then when your cluster gets popped well to be completely safe you have to rebuild the entire ca chain and redistribute new certificates everywhere so wait a second won't that take down the entire cluster sure well some some managed providers will help you with this but even if they do it almost is always going to need some down time so it's
