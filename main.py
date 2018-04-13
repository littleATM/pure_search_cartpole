import gym
import random

ENV = 'CartPole-v0'
action_list = [1 for i in range(1000)]
state_list = [0 for i in range(1000)]
flag_list = [0 for i in range(1000)]


def main():
    index = 0
    env = gym.make(ENV)
    action = env.action_space.n
    env.observation_space
    env.reset()
    env.set_state(0.02, 0.02, 0.02, 0.02)
    state_list[0] = env.get_state()
    print(env.get_state())
    while True:
        # env.set_state(0.02, 0.02, 0.02, 0.02)
        # env.render()
        # continue
        if flag_list[index] == 0:
            action_list[index] = 1
        elif flag_list[index] == 1:
            action_list[index] = (action_list[index] + 1) % 2
        flag_list[index] = flag_list[index] + 1
        if index==2 and flag_list[index]==2:
            x=1
        observation, reward, done, info = env.step(action_list[index])
        print(done)
        print(index)
        print(flag_list[index])
        print(observation)
        state_list[index + 1] = observation
        if done:
            if flag_list[index] == 1:
                # print(state_list)
                # print(state_list[index])
                env.set_state(state_list[index][0], state_list[index][1], state_list[index][2], state_list[index][3])
            elif flag_list[index] == 2:
                temp_index = index
                for i in range(temp_index, -1, -1):
                    if flag_list[i] == 2:
                        flag_list[i] = 0
                        index = index - 1
                    elif flag_list[i] == 1:
                        break
                env.set_state(state_list[index][0], state_list[index][1], state_list[index][2],
                              state_list[index][3])
        else:
            index = index + 1
        # print(env.step(random.randint(0,1)))
        env.render()


if __name__ == "__main__":
    main()
