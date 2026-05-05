---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Taylor Thomas", "Cosmonic", "David Justice", "Microsoft"]
sched_url: https://kccnceu2025.sched.com/event/1tcxS/wasm-i-right-or-wasm-i-wrong-a-review-of-the-wasm-ecosystem-taylor-thomas-cosmonic-david-justice-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Wasm+I+Right+or+Wasm+I+Wrong%3F+a+Review+of+the+Wasm+Ecosystem+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Wasm I Right or Wasm I Wrong? a Review of the Wasm Ecosystem - Taylor Thomas, Cosmonic & David Justice, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Taylor Thomas, Cosmonic, David Justice, Microsoft
- Schedule: https://kccnceu2025.sched.com/event/1tcxS/wasm-i-right-or-wasm-i-wrong-a-review-of-the-wasm-ecosystem-taylor-thomas-cosmonic-david-justice-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Wasm+I+Right+or+Wasm+I+Wrong%3F+a+Review+of+the+Wasm+Ecosystem+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Wasm I Right or Wasm I Wrong? a Review of the Wasm Ecosystem.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcxS/wasm-i-right-or-wasm-i-wrong-a-review-of-the-wasm-ecosystem-taylor-thomas-cosmonic-david-justice-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Wasm+I+Right+or+Wasm+I+Wrong%3F+a+Review+of+the+Wasm+Ecosystem+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KK0FKiQ7nis
- YouTube title: Wasm I Right or Wasm I Wrong? a Review of the Wasm Ecosystem - Taylor Thomas & David Justice
- Match score: 0.888
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/wasm-i-right-or-wasm-i-wrong-a-review-of-the-wasm-ecosystem/KK0FKiQ7nis.txt
- Transcript chars: 30230
- Keywords: assembly, component, wasm, little, ecosystem, projects, components, actually, around, excited, access, language, interfaces, support, standard, write, binary, custom

### Resumo baseado na transcript

As you can see here, this is probably one of my favorite talk titles in the last couple years is was am I right or was am I wrong. Uh maintainer of Run Wisy and Spin Cube uh two CNCF uh based projects for web assembly. Your polyglot because you might need different performance characteristics. Um, obviously as you start to get super high performance, we're not going to talk about that because then every like bit and move matters, but for the general purpose use case, it's not going to affect you. Yeah, the talks tomorrow where they're going to be talking about what they did with the component model, the the challenges they've had with it. Um, hyperllight Wom is really neat because what it does is it provides you a hypervisor boundary around your web assembly components that you can you can execute and use a defense in-depth strategy with extremely low latency and high performance.

### Excerpt da transcript

As you can see here, this is probably one of my favorite talk titles in the last couple years is was am I right or was am I wrong. Um I'm Tara Thomas. This is David. So we'll go ahead and introduce ourselves real quick. Hey, I'm David Justice uh a co-chair for the Wom working group. Uh maintainer of Run Wisy and Spin Cube uh two CNCF uh based projects for web assembly. Uh I'm the author of Go for Dev Ops and a contributor and champion for multiple wy specifications. Uh, also my day job I work at Microsoft as a engineering lead. Yep. And I am Taylor. Like I said, I am also a CNCF WASM working group co-chair. That's why we're giving this talk today. We're not giving it on behalf of our companies. We're mostly giving it on behalf of the working group. Um, and I'm longtime WASOM community member. Uh, I've been involved in uh WASM stuff especially Wom Kubernetes since like 2019 and a longtime contributor in that space along with the various standard specifications. Day jobs. I'm an engineering director at Cosmonic, which is a startup in the web assembly space.

So with that, this ugly slide is purposely ugly because we're not going to spend a lot of time on it. This is the single slide of WASM history. So we we level set. We want to level set here a little bit around what was, how it came to be, and where kind of we are in the evolution. Everything here today is meant to be the unvarnished truth about what like where Web Assembly is at, where where it's being used, those kind of things as we talk about it. And it started in 2013. I know it says 2014 on the ASM.js, but that was the latest available draft and I didn't want to go spelunking for the original draft. So, um that's the very beginning of web assembly and then it it started as ASM.js and then became um web assembly and was integrated into V8. Then it became a draft standard and then it became a core um W3C standard. So, these are all standardsbased things that are in the W3C and it's very important that we understand that. So first off, let's talk about why we have W was in the cloud. We've given these kind of talks before.

So if you've attended these, we're sorry if this is a repeat, but this is very important for the level setting thing. On the left side, you'll see the reasons why web assembly was taken to taken so seriously and then used in the browser so much was because it's an open W3 standard, W3C standard. Like I mentioned, it's sandboxed by default because you're running untrusted code. Um yo
