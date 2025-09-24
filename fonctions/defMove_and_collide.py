def move_and_collide(r, dx, dy, speed, dt, walls):
    # X
    r.x += int(dx * speed * dt)
    for w in walls:
        if r.colliderect(w):
            if dx > 0:  r.right = w.left
            elif dx < 0: r.left  = w.right
    # Y
    r.y += int(dy * speed * dt)
    for w in walls:
        if r.colliderect(w):
            if dy > 0:  r.bottom = w.top
            elif dy < 0: r.top   = w.bottom
