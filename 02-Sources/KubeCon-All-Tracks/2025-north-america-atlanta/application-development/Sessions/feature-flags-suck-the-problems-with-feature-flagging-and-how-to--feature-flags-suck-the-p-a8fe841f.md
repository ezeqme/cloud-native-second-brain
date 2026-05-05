---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Application Development"
themes: ["Application Development"]
speakers: ["Pete Hodgson", "PH1"]
sched_url: https://kccncna2025.sched.com/event/27FdI/feature-flags-suck-the-problems-with-feature-flagging-and-how-to-avoid-them-pete-hodgson-ph1
youtube_search_url: https://www.youtube.com/results?search_query=Feature+Flags+Suck%21+-+The+Problems+With+Feature+Flagging+and+How+To+Avoid+Them+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Feature Flags Suck! - The Problems With Feature Flagging and How To Avoid Them - Pete Hodgson, PH1

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Application Development]]
- Temas: [[Application Development]]
- País/cidade: United States / Atlanta
- Speakers: Pete Hodgson, PH1
- Schedule: https://kccncna2025.sched.com/event/27FdI/feature-flags-suck-the-problems-with-feature-flagging-and-how-to-avoid-them-pete-hodgson-ph1
- Busca YouTube: https://www.youtube.com/results?search_query=Feature+Flags+Suck%21+-+The+Problems+With+Feature+Flagging+and+How+To+Avoid+Them+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Feature Flags Suck! - The Problems With Feature Flagging and How To Avoid Them.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FdI/feature-flags-suck-the-problems-with-feature-flagging-and-how-to-avoid-them-pete-hodgson-ph1
- YouTube search: https://www.youtube.com/results?search_query=Feature+Flags+Suck%21+-+The+Problems+With+Feature+Flagging+and+How+To+Avoid+Them+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=MDERgrcaT6w
- YouTube title: Feature Flags Suck! - The Problems With Feature Flagging and How To Avoid Them - Pete Hodgson, PH1
- Match score: 0.978
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/feature-flags-suck-the-problems-with-feature-flagging-and-how-to-avoid/MDERgrcaT6w.txt
- Transcript chars: 30340
- Keywords: feature, flagging, platform, around, actually, testing, manage, management, making, release, thinking, getting, internal, future, benefit, benefits, organizations, common

### Resumo baseado na transcript

I'm a software delivery consultant, which means I help teams get better at building and releasing software. Open feature is a CNCF project that defines an open standard for feature flagging. And I think that's why uh a lot of organizations get into this problem where when they start with feature flags, it's just a database table and 20 lines of code. The fundamental problem here is as you use feature flags more um you kind of get yourself into a sticky situation which brings us to our second criticism. What can we do differently to u to address this problem, manage our flags better? I I think this comes down to if we break this problem down, it comes down to two main issues.

### Excerpt da transcript

So, hi, my name is Pete Hodgson. I'm a software delivery consultant, which means I help teams get better at building and releasing software. Um, I also serve on the governance board for Open Feature. Open feature is a CNCF project that defines an open standard for feature flagging. You can think of open feature as open telemetry, but for feature flagging. Um, I' I've been on the the open feature governance board since 2022. Um, and I've worked as a consultant for a lot longer than that, kind of talking to organizations about feature flags and continuous delivery. Um, and I' I've noticed this theme, uh, when people talk about feature flags on the internet, um, there's usually some amount of hate and haters in the comments. Um, when people talk about anything on the internet, there's some amount of haters in the comments. um when it comes to to feature flags um that that kind of uh those criticisms tend to break down into two kind of very common themes. So theme number one um it's you know it's just an if else statement.

Um it's I don't even know why we have a name for this. It's a super basic programming practice I've been doing since the dawn of time. Why do you need a framework for this? Why would you pay for a service that does this? Uh it's just a database table and 20 lines of code. Uh, hands up if you've um seen this criticism about feature flags in the past. Uh, hands up if you've made this criticism about feature flags in the past. Okay, second criticism. Um, we use feature flags at my company. We have way too many. They suck. They're awful. Um, there's if statements all over our code. They make a huge mess. No one knows what half these flags do. Some of them don't work and we need to remove them. Some of them, I think, if we change them would break a bunch of stuff. Testing is really hard. Hands up if you've seen this critique of feature flags. Hands up if you've made this critique about feature flags. Okay. So, I want to kind of argue a little bit about about these criticisms, but I want to start by saying I think the people making these points are kind of making them in good faith based on their experience with feature flagging.

Um, but that doesn't mean that these are kind of universal truths for everyone's experience with feature flagging. And one of the points I want to make in this talk is that I think actually not taking feature flags seriously and saying oh it's just an if else statement actually leads to this second issue of not being ab
