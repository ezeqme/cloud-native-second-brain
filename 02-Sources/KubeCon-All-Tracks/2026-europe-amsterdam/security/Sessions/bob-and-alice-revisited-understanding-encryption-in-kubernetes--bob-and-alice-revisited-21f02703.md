---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Security"
themes: ["Security", "Kubernetes Core"]
speakers: ["Jackie Maertens", "Mitch Connors", "Microsoft"]
sched_url: https://kccnceu2026.sched.com/event/2CW1o/bob-and-alice-revisited-understanding-encryption-in-kubernetes-jackie-maertens-mitch-connors-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Bob+and+Alice+Revisited%3A+Understanding+Encryption+in+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Bob and Alice Revisited: Understanding Encryption in Kubernetes - Jackie Maertens & Mitch Connors, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jackie Maertens, Mitch Connors, Microsoft
- Schedule: https://kccnceu2026.sched.com/event/2CW1o/bob-and-alice-revisited-understanding-encryption-in-kubernetes-jackie-maertens-mitch-connors-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Bob+and+Alice+Revisited%3A+Understanding+Encryption+in+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Bob and Alice Revisited: Understanding Encryption in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW1o/bob-and-alice-revisited-understanding-encryption-in-kubernetes-jackie-maertens-mitch-connors-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Bob+and+Alice+Revisited%3A+Understanding+Encryption+in+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Z8SALZo-x0w
- YouTube title: Bob and Alice Revisited: Understanding Encryption in Kubernetes - Jackie Maertens & Mitch Connors
- Match score: 0.885
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/bob-and-alice-revisited-understanding-encryption-in-kubernetes/Z8SALZo-x0w.txt
- Transcript chars: 27454
- Keywords: encryption, public, message, identity, private, certificates, certificate, traffic, symmetric, psyllium, talking, network, actually, authentication, security, identities, messages, secure

### Resumo baseado na transcript

Uh, happy to talk with you all about encryption standards in Kubernetes starting from the ground up. Now, when Jackie and I proposed this talk, which we've proposed a few times, so was it like a year ago that we put together the proposal or so? Um, I'm an ISTO security maintainer and I am our co-lead of the product security working group where we review any CVES or security reports that come in. So that gives us our like three security goals for our secure communication. So through the lens of Alice and Bob, we are going to be examining uh the tools that serve our security goals. And then Mitch is going to take it over and he's going to talk about how these tools map to their to applications within Kubernetes.

### Excerpt da transcript

Well, good morning and welcome everyone. Uh, happy to talk with you all about encryption standards in Kubernetes starting from the ground up. Now, when Jackie and I proposed this talk, which we've proposed a few times, so was it like a year ago that we put together the proposal or so? >> Yeah. >> I had no idea how relevant the talk was going to be uh for me. And that's uh because just yesterday I wake up and I have a text message on my phone from a few hours ago. I'm 8 hours out of my home time zone. And uh the text message is from a number I've never received a message from before, of course, and one of those five-digit numbers. Uh it says that, "Thank you for transferring your 401k, your retirement account, uh out. It's now closed. And if this was in an error, please click this link." The text message came in while I was sleeping. So uh who clicks the link? >> Okay. I have some things to sell you after the talk. You should come meet over here. >> I feel like they're not all being honest. It doesn't even say what company it came from.

Uh, and and with working at different companies over the years, I've had a few different retirement accounts. So, uh, it's not out of the ordinary. Like, I'm married and my spouse manages most of our finances. So, maybe, but we really didn't talk about that in advance. And of course, in the US, it's the middle of the night and they're asleep. For me, what I really needed to know was what is the identity of the person who sent this message? Was this really from a company that I have a financial relationship with? And can I safely reply to them and know who I'm talking to that I'm not giving away financial information and details to a stranger on the internet? Uh, and while encryption might not be the first thing that comes to mind for this, I think I hope by the end of the talk, you'll see how encryption and identity, authorization, and authentication are related as an unbreakable chain. how they're all interdependent on one another and necessary both in our everyday communications. That would be really useful.

If someone comes up with a great standard for text message encryption, let me know. I'd like to use it from now on. Uh but also as we build applications and in Kubernetes. So my name is Mitch Connors. I've been a maintainer of the ISTO project for about seven years now. Uh but I also my day job is I'm a product manager for AKS where I manage networking. And uh I'll take I'll give it to Jackie to take us away with the
